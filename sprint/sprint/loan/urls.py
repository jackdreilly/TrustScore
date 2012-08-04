from django.conf.urls import patterns, include, url
from django.conf import settings
from tastypie.api import Api
from loan.api import LoanResource, PaymentResource, ActorResource, EndorsementResource

api = Api(api_name='v1')
api.register(LoanResource())
api.register(PaymentResource())
api.register(ActorResource())
api.register(EndorsementResource())

urlpatterns = patterns('',

	url(r'^', include(api.urls)),

)