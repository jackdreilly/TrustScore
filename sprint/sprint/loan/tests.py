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
from trust.models import TrustActor, TrustPropagation
from tastypie.test import ResourceTestCase
from django.utils.timezone import make_naive, get_current_timezone
import time
from django.test.utils import get_warnings_state, restore_warnings_state
import warnings
from sprint.util import now

class NewLoan(TestCase, unittest.TestCase):

    def test_create_new_loan(self):
        amount = 10
        borrower = TrustActor(name="jack")
        borrower.save()
        loan = self.create_new_loan(borrower=borrower, amount=amount)

        self.assertFalse(loan.defaulted)
        self.assertEqual(loan.accounted_amount, 0.0)
        self.assertEqual(loan.amount_paid, 0.0)
        self.assertFalse(loan.is_closed)
        self.assertTrue(loan.is_active)

    @classmethod
    def create_new_loan(cls, amount, borrower):
        loan = Loan(actor=borrower, amount=amount)
        loan.save()
        return loan


class NewPayment(TestCase, unittest.TestCase):

    def test_create_new_payment(self):
        loan_amount = 10.0
        borrower = TrustActor(name="jack")
        borrower.save()
        loan = NewLoan.create_new_loan(loan_amount, borrower)
        payment_amount = loan_amount / 2.0
        payment = self.create_new_payment(loan=loan, amount=payment_amount)

    @classmethod
    def create_new_payment(cls, loan, amount):
        payment = Payment(loan=loan, amount=amount)
        payment.save()
        return payment


class NewPaymentPaid(TestCase, unittest.TestCase):

    def setUp(self):
        loan_amount = 10.0
        borrower = TrustActor(name="jack")
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
        paid = PaymentPaidEvent(payment=pmt, amount=amount)
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
        borrower = TrustActor(name="jack")
        borrower.save()
        loan = NewLoan.create_new_loan(loan_amount, borrower)
        payment_amount = loan_amount / 2.0
        payment = NewPayment.create_new_payment(loan=loan, amount=payment_amount)
        self.payment = payment

    def test_create_new_payment_missed(self):
        m_event = self.create_new_payment_missed(self.payment)

    @classmethod
    def create_new_payment_missed(cls, pmt):
        m_event = PaymentMissedEvent(payment=pmt)
        m_event.save()
        return m_event


class FullPaidTest(TestCase, unittest.TestCase):

    def setUp(self):
        loan_amount = 10.0
        borrower = TrustActor(name="jack")
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

    def setUp(self):
        loan_amount = 10.0
        borrower = TrustActor(name="jack")
        borrower.save()
        loan = NewLoan.create_new_loan(loan_amount, borrower)
        endorser = TrustActor(name="john")
        endorser.save()
        loan.receive_endorsement_from_actor(endorser, 1.0)

        borrower.receive_endorsement_from_actor(endorser, 1.0)

        self.assertEqual(len(loan.all_received_endorsements()), 1)
        self.assertEqual(len(borrower.all_received_endorsements()), 1)
        self.assertEqual(len(endorser.all_given_endorsements()), 2)

        payment = loan.new_payment(5.0)
        payment.save()
        payment.complete_payment()

    def test(self):
        borrower = TrustActor.objects.filter(name='jack')[0]
        endorser = TrustActor.objects.filter(name='john')[0]

        self.assertGreater(borrower.trust_score, 1.0)
        self.assertGreater(endorser.trust_score, 1.0)


class ApiTest(ResourceTestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        super(ApiTest, self).setUp()

        self.warnings_state = get_warnings_state()

        # suppress some annoying deprecation warnings caused by the dev version of tastypie
        warnings.filterwarnings('ignore', category=DeprecationWarning, module='django.views.generic.simple')
        warnings.filterwarnings('ignore', category=UserWarning, module='tastypie')

        self.maxDiff = None

        # Create a user.
        self.username = 'foo'
        self.password = 'bar'
        self.user = User.objects.create_user(self.username, 'foo@bar.com', self.password)

    def tearDown(self):
        super(ApiTest, self).tearDown()
        restore_warnings_state(self.warnings_state)

    def get_credentials(self):
        return self.create_basic(username=self.username, password=self.password)


class LoanResourceTest(ApiTest):
    def setUp(self):
        super(LoanResourceTest, self).setUp()

        self.loan_1 = Loan.objects.get(external_id='loan-01')
        self.loan_1_uri = '/api/v1/loan/{0}/'.format(self.loan_1.pk)

        borrower = TrustActor.objects.get(external_id='borrower-01')

        self.post_data = {
            'amount': 99,
            'borrower': '/api/v1/actor/{0}/'.format(borrower.pk),
            'creation_date': now().isoformat(),
            'external_id': "loan-99"
        }

    def test_get_list_unauthorized(self):
        self.assertHttpUnauthorized(self.api_client.get('/api/v1/loan/', format='json'))

    def test_get_list_json(self):
        limit = min(44, Loan.objects.count())
        resp = self.api_client.get('/api/v1/loan/', data={'limit': limit}, format='json', authentication=self.get_credentials())
        self.assertValidJSONResponse(resp)
        self.assertEqual(len(self.deserialize(resp)['objects']), limit)
        i = 0
        for loan in Loan.objects.order_by('id')[:limit]:
            self.assertLoanDetails(self.deserialize(resp)['objects'][i], loan)
            i += 1

    def assertLoanDetails(self, json, loan):
        self.assertEqual(json, {
            u'amount': loan.amount,
            u'id': loan.pk,
            u'description': unicode(loan.description),
            u'borrower': u'/api/v1/actor/{0}/'.format(loan.actor.pk),
            u'creation_date': unicode(make_naive(loan.creation_date, get_current_timezone()).isoformat()),
            u'default_events': [u'/api/v1/loan_default_event/{0}/'.format(event.pk) for event in loan.default_events.all()],
            u'endorsements': [u'/api/v1/endorsement/{0}/'.format(endorsement.pk) for endorsement in loan.endorsements.all()],
            u'external_id': unicode(loan.external_id),
            u'payments': [u'/api/v1/payment/{0}/'.format(payment.pk) for payment in loan.payments.all()],
            u'resource_uri': u'/api/v1/loan/{0}/'.format(loan.pk)
        })

    def test_get_detail_unauthorized(self):
        self.assertHttpUnauthorized(self.api_client.get(self.loan_1_uri, format='json'))

    def test_get_detail_json(self):
        resp = self.api_client.get(self.loan_1_uri, format='json', authentication=self.get_credentials())
        self.assertValidJSONResponse(resp)
        self.assertLoanDetails(self.deserialize(resp), self.loan_1)

    def test_post_list_unauthorized(self):
        self.assertHttpUnauthorized(self.api_client.post('/api/v1/loan/', format='json', data=self.post_data))

    def test_post_list(self):
        count = Loan.objects.count()
        self.assertHttpCreated(self.api_client.post('/api/v1/loan/', format='json', data=self.post_data, authentication=self.get_credentials()))
        self.assertEqual(Loan.objects.count(), count + 1)

    def test_put_detail_unauthorized(self):
        self.assertHttpMethodNotAllowed(self.api_client.put(self.loan_1_uri, format='json', data={}))

    def test_put_detail(self):
        self.assertHttpMethodNotAllowed(self.api_client.put(self.loan_1_uri, format='json', data={}, authentication=self.get_credentials()))
        
    def test_delete_detail_unauthorized(self):
        self.assertHttpMethodNotAllowed(self.api_client.delete(self.loan_1_uri, format='json'))

    def test_delete_detail(self):
        count = Loan.objects.count()
        self.assertHttpMethodNotAllowed(self.api_client.delete(self.loan_1_uri, format='json', authentication=self.get_credentials()))
        self.assertEqual(Loan.objects.count(), count)
