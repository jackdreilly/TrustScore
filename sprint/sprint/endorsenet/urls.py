from django.conf.urls import patterns, include, url
from django.conf import settings
from tastypie.api import Api
from endorsenet.api import SpaceResource, ContextResource, SubjectResource, ActionResource, ActorResource, EndorsementResource

api = Api(api_name='v1')
api.register(SpaceResource())
api.register(ContextResource())
api.register(SubjectResource())
api.register(ActorResource())
api.register(ActionResource())
api.register(EndorsementResource())

urlpatterns = patterns('',

	url(r'^', include(api.urls)),

)