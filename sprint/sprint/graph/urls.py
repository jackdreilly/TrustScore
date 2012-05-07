# urls.py
# =======
from graph.api import *
from django.conf.urls.defaults import patterns, url
from djangorestframework.views import ListOrCreateModelView, InstanceModelView

urlpatterns = patterns('',
    url(r'^api/person/$', ListOrCreateModelView.as_view(resource=PersonResource)),
    url(r'^api/person/(?P<pk>[^/]+)/$', InstanceModelView.as_view(resource=PersonResource)),
    url(r'^api/evaluation/$', ListOrCreateModelView.as_view(resource=EvaluationResource)),
    url(r'^api/evaluation/(?P<pk>[^/]+)/$', InstanceModelView.as_view(resource=EvaluationResource)),
)