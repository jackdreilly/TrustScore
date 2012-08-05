"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import unittest
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase
from loan.models import Loan, Payment, PaymentPaidEvent, PaymentMissedEvent, LoanDefaultEvent
from trust.models import TrustActor


class NewLoan(TestCase, unittest.TestCase):

    def test_create_new_loan(self):
        amount = 10
        borrower  = TrustActor(name = "jack")
        borrower.save()
        loan = self.create_new_loan(borrower = borrower, amount = amount)

        self.assertFalse(loan.defaulted)
        self.assertEqual(loan.accounted_amount, 0.0)
        self.assertEqual(loan.amount_paid, 0.0)
        self.assertFalse(loan.is_closed)
        self.assertTrue(loan.is_active)


    @classmethod
    def create_new_loan(cls, amount, borrower):
        loan = Loan(actor = borrower, amount = amount)
        loan.save()
        return loan


class NewPayment(TestCase, unittest.TestCase):

    def test_create_new_payment(self):
        loan_amount = 10.0
        borrower  = TrustActor(name = "jack")
        borrower.save()
        loan = NewLoan.create_new_loan(loan_amount, borrower)
        payment_amount = loan_amount / 2.0
        payment = self.create_new_payment(loan=loan, amount=payment_amount)

    @classmethod
    def create_new_payment(cls, loan, amount):
        payment  = Payment(loan=loan, amount=amount)
        payment.save()
        return payment

class NewPaymentPaid(TestCase, unittest.TestCase):

    def setUp(self):
        loan_amount = 10.0
        borrower  = TrustActor(name = "jack")
        borrower.save()
        loan = NewLoan.create_new_loan(loan_amount, borrower)
        payment_amount = loan_amount / 2.0
        payment = NewPayment.create_new_payment(loan=loan, amount=payment_amount)
        self.payment = payment        

    def test_create_new_payment_paid_full(self):
        paid_amount = self.payment.amount
        paid = self.create_new_payment_paid(self.payment, paid_amount)

        self.assertTrue(self.payment.is_closed)
        self.assertFalse(self.payment.is_active)
        self.assertEqual(self.payment.amount_paid, self.payment.loan.amount_paid)
        self.assertTrue(self.payment.loan.is_active)

    @classmethod
    def create_new_payment_paid(cls, pmt, amount):
        paid  = PaymentPaidEvent(payment=pmt, amount=amount)
        paid.save()
        return paid

    def test_multiple_payments(self):
        payment = self.payment
        amount = payment.amount
        n_splits = 5
        splits = [amount / float(n_splits) for _ in range(n_splits)]
        paids = [
            self.create_new_payment_paid(payment, paid_amount)
            for paid_amount in splits
        ]
        [paid.save() for paid in paids]

        self.assertTrue(payment.is_closed)

class NewPaymentMissed(TestCase, unittest.TestCase):

    def setUp(self):
        loan_amount = 10.0
        borrower  = TrustActor(name = "jack")
        borrower.save()
        loan = NewLoan.create_new_loan(loan_amount, borrower)
        payment_amount = loan_amount / 2.0
        payment = NewPayment.create_new_payment(loan=loan, amount=payment_amount)
        self.payment = payment        

    def test_create_new_payment_missed(self):
        m_event = self.create_new_payment_missed(self.payment)

    @classmethod
    def create_new_payment_missed(cls, pmt):
        m_event  = PaymentMissedEvent(payment=pmt)
        m_event.save()
        return m_event

class FullPaidTest(TestCase, unittest.TestCase):

    def setUp(self):
        loan_amount = 10.0
        borrower  = TrustActor(name = "jack")
        borrower.save()
        loan = NewLoan.create_new_loan(loan_amount, borrower)
        n_splits = 5
        splits = [loan_amount / float(n_splits) for _ in range(n_splits)]
        pmts = [
            NewPayment.create_new_payment(loan, pmt_amount)
            for pmt_amount in splits
        ]
        for pmt in pmts:
            pmt.complete_payment()

        self.loan = loan

    def test_result(self):
        loan = self.loan

        self.assertTrue(loan.is_closed)

        for pmt in loan.all_payments:
            self.assertTrue(pmt.is_closed)


class EndorsingTest(TestCase, unittest.TestCase):

    def test(self):
        loan_amount = 10.0
        borrower  = TrustActor(name = "jack")
        borrower.save()
        loan = NewLoan.create_new_loan(loan_amount, borrower)
        endorser  = TrustActor(name = "john")
        endorser.save()

        loan.receive_endorsement_from_actor(endorser, 1.0)

        borrower.receive_endorsement_from_actor(endorser, 1.0)

        self.assertEqual(len(loan.all_received_endorsements()), 1)
        self.assertEqual(len(borrower.all_received_endorsements()), 1)
        self.assertEqual(len(endorser.all_given_endorsements()), 2)