from trust_test import *
import pylab as lab

def good_then_default():
    loan = Loan(100.)

    payment = loan.new_payment(10.0)
    payment.new_event(Event.paid(0.0, 10.0))

    payment = loan.new_payment(10.0)
    payment.new_event(Event.paid(0.0, 10.0))

    payment = loan.new_payment(10.0)
    payment.new_event(Event.missed(1.0))
    payment.new_event(Event.missed(1.0))

    payment.new_event(Event.paid(3.0, 5.0))
    payment.new_event(Event.missed(2.0))
    payment.new_event(Event.paid(6.0, 5.0))

    loan.default()
    lab.plot(loan.trust_profile())
    lab.show()
    
def never_pay_last(last_pay_time=5.0):
    loan = Loan(100.0)
    
    payment = loan.new_payment(50)
    
    payment.new_event(Event.paid(0.0,50.0))
    
    payment = loan.new_payment(40)

    payment.new_event(Event.paid(0.0,40.0))
    
    payment = loan.new_payment(10)
    
    payment.new_event(Event.missed(1.0))
    payment.new_event(Event.missed(1.0))
    payment.new_event(Event.missed(1.0))
    payment.new_event(Event.missed(1.0))
    payment.new_event(Event.missed(1.0))
    payment.new_event(Event.missed(1.0))
    
    payment.new_event(Event.paid(last_pay_time, 10.0))
    return loan
    
def compare_npl(times=None):
    if times is None:
        times = lab.linspace(0.0, 10, 5)
    lab.figure()
    lab.hold(True)
    for time in times:
        lab.plot(never_pay_last(time).trust_profile(), label = str(time))
    lab.legend(loc=4)
    lab.show()

def bum(default=True):
    loan = Loan(100.0)
    n = 10
    nn = 2
    m = 10.0
    dt = 1.0
    for _ in range(n):
        loan.new_payment(m)
        loan.missed_all_open_payments(dt)
    for _ in range(nn):
        loan.missed_all_open_payments(dt)
    if default:
        loan.default()
    return loan
    
def bum_compare():
    lab.figure()
    lab.hold(True)
    lab.plot(bum(False).trust_profile(), label='no def')
    lab.plot(bum(True).trust_profile(), label='def')
    lab.legend()
    lab.show()
    
def late_every_month(dt = 3.0, t = 4.0):
    loan = Loan(100.0)
    
    lab.figure()
    lab.hold(True)
    
    for i in range(10):
        payment = loan.new_payment(10.0)
        for i in range(3):
            payment.new_event(Event.missed(float(dt)/3.0))
        payment.new_event(Event.paid(t, 10.0))
    lab.plot(loan.trust_profile(), label='late')
    loan = Loan(100.0)
    
    for i in range(10):
        payment = loan.new_payment(10.0)
        payment.new_event(Event.paid(0.0, 10.0))
    lab.plot(loan.trust_profile(), label='on time')
    
    lab.legend()
    lab.show()
    
# late_every_month()
# bum_compare()
# compare_npl()    
good_then_default()
    