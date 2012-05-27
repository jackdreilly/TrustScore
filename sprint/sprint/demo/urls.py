from django.conf.urls import patterns, url, include
from views import AgentView, LoanView, HomeView

urlpatterns = patterns('',
    (r'^agent/(?P<pk>[^/]+)/$', AgentView.as_view()),
    (r'^loan/(?P<pk>[^/]+)/$', LoanView.as_view()),
    (r'^$', HomeView.as_view()),
)