from django.conf.urls import patterns, url, include
from views import AgentView, LoanView

urlpatterns = patterns('',
    (r'^agent/(?P<pk>[^/]+)/$', AgentView.as_view()),
    (r'^loan/(?P<pk>[^/]+)/$', LoanView.as_view()),
)