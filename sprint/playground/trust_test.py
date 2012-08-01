import math

def cum_sum(lst):
    next = [0.0]
    for l in lst:
        next.append(next[-1] + l)
    return next

class Loan(object):
    """docstring for Loan"""
    
    FLOOR_SCALE = 1.0
    CEILING_SCALE = 1.0
    
    def __init__(self, amount):
        super(Loan, self).__init__()
        self.amount = amount
        self.payments = []
        self.accounted = 0.0
        self.paid = 0.0
        self.defaulted = False
        self.open_payments = set()
        self.closed_payments = set()
        
    def missed_all_open_payments(self, dt):
        for payment in self.open_payments:
            payment.new_event(Event.missed(dt))
        
    def trust_scores(self):
        return [event.trust_score for payment in self.payments for event in payment.events]
        
    def trust_profile(self):
        return cum_sum(self.trust_scores())
        
    @property
    def trust_floor(self):
        return -1.0 * self.FLOOR_SCALE * self.amount
        
    def floor_fn(self, amount):
        return (math.exp(amount / self.amount) - 1) / (math.exp(1.0) - 1)
        
    def payment_floor_factor(self, amount):
        print 'amount', amount
        v1 = self.floor_fn(self.accounted + amount)
        v2 =  self.floor_fn(self.accounted)
        print 'v1', v1
        print 'v2', v2
        print ''
        return v1 - v2
        
    def ceiling_fn(self, amount):
        return amount / self.trust_ceiling
    
    def payment_ceiling_factor(self, amount):
        return self.ceiling_fn(self.accounted + amount) - self.ceiling_fn(self.accounted)
        
    @property
    def trust_ceiling(self):
        return self.CEILING_SCALE * self.amount
        
    def new_payment(self, amount):
        loan = self
        floor = self.payment_floor_factor(amount) * self.trust_floor
        ceiling = self.payment_ceiling_factor(amount) * self.trust_ceiling
        payment = Payment(loan, amount, floor, ceiling)
        self.add_new_payment(payment)
        self.accounted+=amount
        return payment
        
    def add_new_payment(self, payment):
        self.payments.append(payment)
        self.open_payments.add(payment)
        
    def default(self):
        self.defaulted = True
        self.new_payment(self.amount - self.accounted)
        for payment in self.open_payments:
            payment.default()
        
            
    def payment_finished(self, payment):
        self.open_payments.remove(payment)
        self.closed_payments.add(payment)
        
        
        
class Payment(object):
    """docstring for Payment"""
    
    DEFAULT_WEIGHT = 2.0
    PAID_DECAY_RATE = 10.0
    MISSED_DECAY_RATE = 2.0
    
    def __init__(self, loan, amount, floor = None, ceiling = None):
        super(Payment, self).__init__()
        print loan, amount, floor, ceiling
        if floor is None:
            floor = -amount
        if ceiling is None:
            ceiling = amount
        self.loan = loan
        self.floor = floor
        self.ceiling = ceiling
        self.t = 0
        self.events = []
        self.paid = 0
        self.amount = amount
        self.defaulted = False
    
    @property
    def missed_pool(self):
        return self.floor / self.DEFAULT_WEIGHT
        
    def missed_fn(self, dt):
        start = self.t
        stop = start + dt
        self.t+=dt
        factor = self.missed_factor(start, stop)
        penalty = factor * self.missed_pool
        return penalty
        
         
    def missed_factor(self, start, stop):
        return math.exp(-start/self.MISSED_DECAY_RATE) - math.exp(-stop/self.MISSED_DECAY_RATE)

        
    def paid_fn(self, t, amount):
        self.paid+=amount
        if self.paid >= self.amount:
            self.loan.payment_finished(self)
        t_paid_factor = self.paid_factor(t)
        total_factor = t_paid_factor * amount / self.amount
        reward = total_factor * self.ceiling
        return reward
        
    def new_event(self, event):
        e_type = event.e_type
        if e_type is Event.Type.PAID:
            event.trust_score = self.paid_fn(event.t, event.amount)
        elif e_type is Event.Type.MISSED:
            event.trust_score = self.missed_fn(event.dt)
        elif e_type is Event.Type.DEFAULT:
            event.trust_score = self.default_fn()
        self.events.append(event)
        
        
    def default_fn(self):
        self.defaulted = True
        prev_scores = sum(event.trust_score for event in self.events)
        default_score = self.floor
        score = default_score - prev_scores
        return score
        
    def default(self):
        self.new_event(Event.default())
         
    def paid_factor(self, t):
        return math.exp(-t/ self.PAID_DECAY_RATE)

class Event(object):
    """docstring for Event"""
    
    class Type(object):
        PAID = 0
        MISSED = 1
        DEFAULT = 2 
    
    def __init__(self, e_type, t = None, dt = None, amount = None):
        super(Event, self).__init__()
        self.e_type = e_type
        self.t = t
        self.dt = dt
        self.amount = amount
        
    @classmethod
    def default(cls):
        return cls(e_type = cls.Type.DEFAULT)
        
    @classmethod
    def paid(cls, t, amount):
        return cls(cls.Type.PAID, t = t, amount = amount)
        
    @classmethod
    def missed(cls, dt):
        return cls(cls.Type.MISSED, dt = dt)