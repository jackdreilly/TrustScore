from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.conf.urls import url
from tastypie.http import HttpGone, HttpMultipleChoices
from tastypie import fields
from tastypie.utils import trailing_slash
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from endorsenet.models import Endorsement
from trust.models import TrustActor
from loan.models import Loan, Payment, LoanDefaultEvent, PaymentPaidEvent, PaymentMissedEvent, PaymentTrustEvent
import inflection

class MyModelResource(ModelResource):
	def prepend_urls(self):
		urls = []
	
		for name, field in self.fields.items():
			if isinstance(field, fields.ToManyField):
				resource = r"^(?P<resource_name>{resource_name})/(?P<{related_name}>.+)/{related_resource}/$".format(
					resource_name = self._meta.resource_name,
					related_name = field.related_name,
					related_resource = self.get_class(field.to)._meta.resource_name,
				)
				resource = url(resource, field.to_class().wrap_view('dispatch_list'), name="api_dispatch_detail")
				urls.append(resource)
		return urls

	def get_class(self, kls):
		if not isinstance(kls, str):
			return kls

		parts = kls.split('.')
		module = ".".join(parts[:-1])
		m = __import__(module)
		for comp in parts[1:]:
			m = getattr(m, comp)            
		return m

class LoanResource(MyModelResource):
	class Meta:
		queryset = Loan.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()
		filtering = {
			"borrower": ('exact')
		}
		allowed_methods = ['get', 'post']

	endorsements = fields.ToManyField('loan.api.EndorsementResource', 'received_endorsements', related_name = 'loan', full = False, null = True) 
	borrower = fields.ToOneField('loan.api.ActorResource', 'actor', full = False)
	payments = fields.ToManyField('loan.api.PaymentResource', 'payments', 'loan', full = False, null = True)
	default_events = fields.ToManyField('loan.api.LoanDefaultEventResource', 'default_events', 'loan', full = False, null = True)

class PaymentResource(MyModelResource):
	class Meta:
		queryset = Payment.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()
		filtering = {
			"loan": ('exact')
		}
		allowed_methods = ['get', 'post']

	loan = fields.ToOneField('loan.api.LoanResource', 'loan', full = False)
	paid_events = fields.ToManyField('loan.api.PaymentPaidEventResource', 'paid_events', 'payment', full = False)
	missed_events = fields.ToManyField('loan.api.PaymentMissedEventResource', 'missed_events', 'payment', full = False)
	
class EndorsementResource(MyModelResource):
	class Meta:
		queryset = Endorsement.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()
		filtering = {
			"loan": ('exact'),
			"trustee": ('exact')
		}
		allowed_methods = ['get', 'post']

	loan = fields.ToOneField('loan.api.LoanResource', 'subject', related_name = 'received_endorsements', full = False, null = True) 
	trustee = fields.ToOneField('loan.api.ActorResource', 'endorser', related_name = 'given_endorsements', full = False, null = True) 
	
class ActorResource(MyModelResource):
	class Meta:
		resource_name = 'actor'
		queryset = TrustActor.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()
		allowed_methods = ['get', 'post']

	endorsements = fields.ToManyField('loan.api.EndorsementResource', 'given_endorsements', related_name = 'endorser', full = False, null = True) 
	loans_received = fields.ToManyField('loan.api.LoanResource', 'actions', related_name = 'actor', full = False, null = True) 

class LoanDefaultEventResource(MyModelResource):
	class Meta:
		resource_name = 'loan_default_event'
		queryset = LoanDefaultEvent.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()
		filtering = {
			"loan": ('exact')
		}
		allowed_methods = ['get', 'post']
		
	loan = fields.ToOneField('loan.api.LoanResource', 'loan', full = False)

class PaymentPaidEventResource(MyModelResource):
	class Meta:
		resource_name = 'payment_paid_event'
		queryset = PaymentPaidEvent.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()
		filtering = {
			"payment": ('exact')
		}
		allowed_methods = ['get', 'post']

	payment = fields.ToOneField('loan.api.PaymentResource', 'payment', full = False)

class PaymentMissedEventResource(MyModelResource):
	class Meta:
		resource_name = 'payment_missed_event'
		queryset = PaymentMissedEvent.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()
		filtering = {
			"payment": ('exact')
		}
		allowed_methods = ['get', 'post']
		
	payment = fields.ToOneField('loan.api.PaymentResource', 'payment', full = False)

