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
from loan.models import Loan, Payment, PaymentPaidEvent, PaymentMissedEvent
import inflection

class MyModelResource(ModelResource):
	def override_urls(self):
		urls = []
	
		for name, field in self.fields.items():
			if isinstance(field, fields.ToManyField):
				resource = r"^(?P<resource_name>{resource_name})/(?P<{related_name}>.+)/{related_resource}/$".format(
					resource_name = self._meta.resource_name, 
					related_name = field.related_name ,
					related_resource = inflection.singularize(field.attribute),
					)
				print resource
				resource = url(resource, field.to_class().wrap_view('dispatch_list'), name="api_dispatch_detail")
				urls.append(resource)
		return urls

class LoanResource(MyModelResource):
	class Meta:
		queryset = Loan.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()

	endorsements = fields.OneToManyField('loan.api.EndorsementResource', 'received_endorsements', related_name = 'loan', full = False, null = True) 
	borrower = fields.ToOneField('loan.api.ActorResource', 'actor', full = False)
	payments = fields.ToManyField('loan.api.PaymentResource', 'payments', 'loan', full = False)

class PaymentResource(MyModelResource):
	class Meta:
		queryset = Payment.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()
		filtering = {
			"loan": ('exact')
		}

	loan = fields.ToOneField('loan.api.LoanResource', 'loan', full = False)

class EndorsementResource(MyModelResource):
	class Meta:
		queryset = Endorsement.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()

	loan = fields.ToOneField('loan.api.LoanResource', 'subject', related_name = 'received_endorsements', full = False, null = True) 
	trustee = fields.ToOneField('loan.api.ActorResource', 'endorser', related_name = 'given_endorsements', full = False, null = True) 
	
class ActorResource(MyModelResource):
	class Meta:
		resource_name = 'actor'
		queryset = TrustActor.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()

	endorsements = fields.ToManyField('loan.api.EndorsementResource', 'given_endorsements', related_name = 'endorser', full = False, null = True) 
	loans_received = fields.OneToManyField('loan.api.LoanResource', 'actions', related_name = 'actor', full = False, null = True) 