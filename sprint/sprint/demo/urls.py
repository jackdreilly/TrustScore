from django.conf.urls import patterns, url, include
from views import AgentView

urlpatterns = patterns('',
    (r'^agent/(?P<pk>[^/]+)/$', AgentView.as_view()),
)