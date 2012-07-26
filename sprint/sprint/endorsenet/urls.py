from django.conf.urls import patterns, include, url
from django.conf import settings
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from endorsenet.resources import SpaceResource, ContextResource, ActorResource, ActionResource, EndorsementResource

urlpatterns = patterns('',

	url(r'^spaces$', ListOrCreateModelView.as_view(resource=SpaceResource), name='space-resource-root'),
	url(r'^spaces/(?P<space>[^/]+)/$', InstanceModelView.as_view(resource=SpaceResource)),

	url(r'^spaces/(?P<space>[^/]+)/contexts$', ListOrCreateModelView.as_view(resource=ContextResource), name='context-resource-root'),
	url(r'^spaces/(?P<space>[^/]+)/contexts/(?P<context>[^/]+)/$', InstanceModelView.as_view(resource=ContextResource)),

	url(r'^spaces/(?P<space>[^/]+)/contexts/(?P<context>[^/]+)/actors$', ListOrCreateModelView.as_view(resource=ActorResource), name='actor-resource-root'),
	url(r'^spaces/(?P<space>[^/]+)/contexts/(?P<context>[^/]+)/actors/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=ActorResource)),

	url(r'^spaces/(?P<space>[^/]+)/contexts/(?P<context>[^/]+)/actions$', ListOrCreateModelView.as_view(resource=ActionResource), name='action-resource-root'),
	url(r'^spaces/(?P<space>[^/]+)/contexts/(?P<context>[^/]+)/actions/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=ActionResource)),

	url(r'^spaces/(?P<space>[^/]+)/contexts/(?P<context>[^/]+)/endorsements$', ListOrCreateModelView.as_view(resource=EndorsementResource), name='endorsement-resource-root'),
	url(r'^spaces/(?P<space>[^/]+)/contexts/(?P<context>[^/]+)/endorsements/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=EndorsementResource)),

)