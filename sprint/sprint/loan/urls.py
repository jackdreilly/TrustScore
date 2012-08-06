from django.conf.urls import patterns, include, url
from django.conf import settings
from tastypie.api import Api
from loan.api import LoanResource, PaymentResource, ActorResource, EndorsementResource, LoanDefaultEventResource, PaymentPaidEventResource, PaymentMissedEventResource, PaymentTrustEventResource

api = Api(api_name='v1')
api.register(LoanResource())
api.register(PaymentResource())
api.register(ActorResource())
api.register(EndorsementResource())
api.register(LoanDefaultEventResource())
api.register(PaymentPaidEventResource())
api.register(PaymentMissedEventResource())
api.register(PaymentTrustEventResource())

urlpatterns = patterns('',

	url(r'^', include(api.urls)),

)