from django.db import models
import sprint.trust.models as t_models
import datetime
from django.utils.timezone import utc
import math
from process_mixin import ProcessAfterSaveMixin
from sprint.auto_print import AutoPrintMixin

def now():
    return datetime.datetime.utcnow().replace(tzinfo=utc)


class Loan(t_models.TrustAction):
    amount = models.FloatField()
    
    FLOOR_SCALE = 1.0
    CEILING_SCALE = 1.0

    class Status:
        ACTIVE = 0
        CLOSED = 1
        DEFAULTED = 2

    @classmethod
    def get_loans_for_actor(self, actor):
        return Loan.objects.filter(actor=actor)

    @property
    def trust_floor(self):
        return -1.0 * self.FLOOR_SCALE * self.amount

    def floor_fn(self, amount):
        # the proportion of the entire penalty pool to assign to the current loan
        return (math.exp(amount / self.amount) - 1) / (math.exp(1.0) - 1)

    def payment_floor_factor(self, amount): 
        return self.floor_fn(self.accounted_amount + amount) - self.floor_fn(self.accounted_amount)

    def ceiling_fn(self, amount):
        return amount / self.trust_ceiling

    def payment_ceiling_factor(self, amount):
        return self.ceiling_fn(self.accounted_amount + amount) - self.ceiling_fn(self.accounted_amount)
        
    def new_payment(self, amount):
        loan = self
        floor = self.floor_from_amount(amount)
        ceiling = self.ceiling_from_amount(amount) 
        payment = Payment(loan=loan, amount=amount, floor=floor, ceiling=ceiling)
        self.add_new_payment(payment)
        return payment

    def floor_from_amount(self, amount):
        return self.payment_floor_factor(amount) * self.trust_floor

    def ceiling_from_amount(self, amount):
        return self.payment_ceiling_factor(amount) * self.trust_ceiling
        
    def default(self):
        default = LoanDefaultEvent(loan = self)
        default.save()

    def process_default_event(self, event):
        self.new_payment(self.amount - self.accounted_amount)
        for payment in self.active_payments:
            payment.process_default_event(event)

    @property
    def status(self):
        if self.is_closed:
            return self.Status.CLOSED
        if self.defaulted:
            return self.Status.DEFAULTED
        return self.Status.ACTIVE
            
    @property
    def defaulted(self):
        return len(
            self.default_events()
        ) > 0
        
    def default_events(self):
        return LoanDefaultEvent.objects.filter(loan=self).all()
        
    def add_new_payment(self, payment):
        payment.save()

    @property
    def trust_ceiling(self):
        return self.CEILING_SCALE * self.amount
    
    @property
    def active_payments(self):
        return [
            payment
            for payment in self.all_payments
            if payment.is_active
        ]
        
        
    def missed_active_payments(self, time = None):
        for payment in self.active_payments:
            payment.missed_payment

        
    def closed_payment(self):
        return [
            payment
            for payment in self.all_payments
            if payment.is_closed
        ]
    
    @property    
    def all_payments(self):
        return self.payments.all()
        
    @property
    def is_active(self):
        return self.amount_paid < self.amount

    @property
    def is_closed(self):
        return not self.is_active
        
    @property
    def amount_paid(self):
        return sum(
            payment.amount_paid
            for payment in self.all_payments
        )
        
    @property
    def accounted_amount(self):
        return sum(
            payment.amount
            for payment in self.all_payments
        )
    
class Payment(AutoPrintMixin, models.Model):
    loan = models.ForeignKey(Loan, related_name="payments")
    amount = models.FloatField()
    floor = models.FloatField(blank=True)
    ceiling = models.FloatField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    due_date = models.DateTimeField(blank=True)

    DEFAULT_PAYMENT_DAYS = 1

    DEFAULT_WEIGHT = 2.0
    PAID_DECAY_RATE = 100000.0
    MISSED_DECAY_RATE = 200000.0

    def to_string(self):
        return 'loan: {0}, amount: {1}, due_date: {2}'.format(self.loan.pk, self.amount, self.due_date)

    def save(self, *args, **kwargs):
        if not self.floor:
            self.floor = self.calculate_floor()
        if not self.ceiling:
            self.ceiling = self.calculate_ceiling()
        if not self.due_date:
            if not self.creation_date:
                self.creation_date = now()
            self.due_date = self.creation_date + datetime.timedelta(self.DEFAULT_PAYMENT_DAYS)
        super(Payment, self).save(*args, **kwargs)

    def calculate_floor(self):
        return self.loan.floor_from_amount(self.amount)

    def calculate_ceiling(self):
        return self.loan.ceiling_from_amount(self.amount)
    
    def prev_missed_date(self, missed_event):
        query = PaymentMissedEvent.objects.filter(payment=self).filter(date__lt=missed_event.date).order_by('-date')
        if len(query) < 1:
            return missed_event.date
        return query[0].date
    
    @property
    def amount_paid(self):
        return sum(
            event.amount
            for event in self.paid_events
        )
        
    @property
    def missed_pool(self):
        return self.floor / self.DEFAULT_WEIGHT

    def process_missed_event(self, missed_event):
        start = self.prev_missed_date(missed_event)
        stop = missed_event.date
        sec_start = self.seconds_from_start(start)
        sec_stop = self.seconds_from_start(stop)
        factor = self.missed_factor(sec_start, sec_stop)
        penalty = factor * self.missed_pool
        self.create_trust_event(penalty)

    def missed_factor(self, start, stop):
        return math.exp(-start/self.MISSED_DECAY_RATE) - math.exp(-stop/self.MISSED_DECAY_RATE)
        
    def seconds_from_start(self, time):
        return (time - self.due_date).total_seconds()

    def process_paid_event(self, paid_event):
        time = self.seconds_from_start(paid_event.date)
        if time < 0.0:
            # the paid event happened before the due date, just change t to 0
            time = 0.0
        amount = paid_event.amount
        t_paid_factor = self.paid_factor(time)
        total_factor = t_paid_factor * amount / self.amount
        reward = total_factor * self.ceiling
        self.create_trust_event(reward)
        
    def missed_payment(self):
        return self.new_missed_event()
        
    @property
    def paid_events(self):
        return PaymentPaidEvent.objects.filter(payment=self).all()

    @property
    def all_payment_events(self):
        return self.payment_event_set.all()

    @property
    def all_trust_events(self):
        return self.paymenttrustevent_set.all()
        
    @property
    def is_active(self):
        return self.amount_paid < self.amount
    
    @property
    def is_closed(self):
        return not self.is_active
    
    @property
    def missed_events(self):
        return PaymentMissedEvent.objects.filter(payment=self).all()

    def create_missed_event(self, date = None):
        if date is None:
            date = now()
        missed_event = PaymentMissedEvent(payment=self, date = date)
        missed_event.save()
        return missed_event

    def process_default_event(self, event):
        prev_scores = sum(t_event.score for t_event in self.all_trust_events)
        default_score = self.floor
        penalty = default_score - prev_scores
        self.create_trust_event(penalty)

    def create_trust_event(self, score):
        event = PaymentTrustEvent(action=self.loan, payment=self, score=score)
        event.save()
        return event
        
    @property
    def defaulted(self):
        return self.loan.defaulted

    def paid_factor(self, t):
        return math.exp(-t/ self.PAID_DECAY_RATE)

    @property
    def amount_left_to_pay(self):
        return self.amount - self.amount_paid

    def complete_payment(self):
        complete_amount = self.amount_left_to_pay
        event = PaymentPaidEvent(payment = self,amount = complete_amount)
        event.save()
        return event

class PaymentTrustEvent(t_models.TrustEvent):
    payment = models.ForeignKey(Payment)

    def to_string(self):
        return 'pmnt: {0}, rest: {1}'.format(self.payment.pk, super(PaymentTrustEvent, self))

class PaymentEvent(AutoPrintMixin, ProcessAfterSaveMixin, models.Model):
    payment = models.ForeignKey(Payment)
    date = models.DateTimeField(auto_now_add=True, null=True, blank =True)

    def to_string(self):
        return 'pmnt: {0}, date: {1}'.format(self.payment.pk, self.date)
    
class PaymentPaidEvent(PaymentEvent):
    amount = models.FloatField()

    def process(self):
        self.payment.process_paid_event(self)

    def to_string(self):
        return 'pmnt: {0}, date: {1}, amount: {2}'.format(self.payment.pk, self.date, self.amount)
    
class PaymentMissedEvent(PaymentEvent):
    
    def process(self):
        self.payment.process_missed_event(self)

class LoanEvent(AutoPrintMixin, ProcessAfterSaveMixin, models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True, blank =True)
    loan = models.ForeignKey(Loan)

    def to_string(self):
        return 'loan: {0}, date: {1}'.format(self.loan.pk, self.date)
    
class LoanDefaultEvent(LoanEvent):
    
    def process(self):
        self.loan.process_default_event(self)
