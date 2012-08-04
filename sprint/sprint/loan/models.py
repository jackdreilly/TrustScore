from django.db import models
import sprint.trust.models as t_models
from datetime import datetime
import math

class Loan(t_models.TrustAction):
    amount = models.FloatField()
    
    FLOOR_SCALE = 1.0
    CEILING_SCALE = 1.0

    @property
    def trust_floor(self):
        return -1.0 * self.FLOOR_SCALE * self.amount

    def floor_fn(self, amount):
        # the proportion of the entire penalty pool to assign to the current loan
        return (math.exp(amount / self.amount) - 1) / (math.exp(1.0) - 1)

    def payment_floor_factor(self, amount): 
        return self.floor_fn(self.accounted + amount) - self.floor_fn(self.accounted)

    def ceiling_fn(self, amount):
        return amount / self.trust_ceiling

    def payment_ceiling_factor(self, amount):
        return self.ceiling_fn(self.accounted + amount) - self.ceiling_fn(self.accounted)
        
    def new_payment(self, amount):
        loan = self
        floor = self.payment_floor_factor(amount) * self.trust_floor
        ceiling = self.payment_ceiling_factor(amount) * self.trust_ceiling
        payment = Payment(loan=loan, amount=amount, floor=floor, ceiling=ceiling)
        self.add_new_payment(payment)
        return payment
        
    def default(self):
        default = LoanDefaultEvent(loan = self)
        default.save()
            
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
    
    def active_payments(self):
        return [
            payment
            for payment in self.all_payments()
            if payment.is_active()
        ]
        
        
    def missed_active_payments(self, time = None):
        for payment in self.active_payments():
            payment.missed_payment()

        
    def closed_payment(self):
        return [
            payment
            for payment in self.all_payments()
            if payment.is_closed()
        ]
        
    def all_payments(self):
        return self.payment_set.all()
        
    def is_active(self):
        return self.amount_paid() >= self.amount
        
    def amount_paid(self):
        return sum(
            payment.amount_paid()
            for payment in self.all_payments()
        )
        
    def accounted_amount(self):
        return sum(
            payment.amount
            for payment in self.all_payments()
        )
    
class Payment(models.Model):
    loan = models.ForeignKey(Loan)
    amount = models.FloatField()
    floor = models.FloatField()
    ceiling = models.FloatField()
    due_date = models.DateTimeField(auto_now_add=True)

    DEFAULT_WEIGHT = 2.0
    PAID_DECAY_RATE = 10.0
    MISSED_DECAY_RATE = 2.0
    
    def defaulted(self):
        return len(self.default_events()) > 0
    
    def prev_missed_date(self, missed_event):
        query = PaymentMissedEvent.objects.filter(payment=self).filter(date__lt=missed_event.date).order_by('-date')
        if len(query) < 1:
            return missed_event.date
        return query[0].date
    
    def amount_paid(self):
        return sum(
            event.amount
            for event in self.paid_events()
        )
        
    @property
    def missed_pool(self):
        return self.floor / self.DEFAULT_WEIGHT

    def missed_fn(self, missed_event):
        start = self.last_missed_date(missed_event)
        stop = missed_event.date
        sec_start = self.seconds_from_start(start)
        sec_stop = self.seconds_from_start(stop)
        factor = self.missed_factor(sec_start, sec_stop)
        penalty = factor * self.missed_pool
        return penalty

    def missed_factor(self, start, stop):
        return math.exp(-start/self.MISSED_DECAY_RATE) - math.exp(-stop/self.MISSED_DECAY_RATE)
        
    def seconds_from_start(self, time):
        return (time - self.due_date).total_seconds()

    def paid_fn(self, paid_event):
        time = self.seconds_from_start(paid_event.date)
        amount = paid_event.amount
        t_paid_factor = self.paid_factor(time)
        total_factor = t_paid_factor * amount / self.amount
        reward = total_factor * self.ceiling
        return reward
        
    def missed_payment(self):
        return self.new_missed_event()
        
    def paid_events(self):
        return PaymentPaidEvent.objects.filter(payment=self).all()
        
    def is_active(self):
        return self.amount_paid() >= self.amount
        
    def is_closed(self):
        return not self.is_active()
    
    def missed_events(self):
        return PaymentMissedEvent.objects.filter(payment=self).all()

    def create_missed_event(self, date = None):
        if date is None:
            date = datetime.now()
        missed_event = PaymentMissedEvent(payment=self, date = date)
        missed_event.save()
        return missed_event
        
    def defaulted(self):
        return self.loan.defaulted()

    def paid_factor(self, t):
        return math.exp(-t/ self.PAID_DECAY_RATE)


class LoanEvent(models.Model):
    date = models.DateTimeField()
    loan = models.ForeignKey(Loan)

class PaymentEvent(models.Model):
    payment = models.ForeignKey(Payment)
    date = models.DateTimeField()
    
class PaymentPaidEvent(PaymentEvent):
    amount = models.FloatField()
    
class PaymentMissedEvent(PaymentEvent):
    pass
    
class LoanDefaultEvent(LoanEvent):
    pass