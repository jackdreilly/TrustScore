from django.conf.urls import patterns, url, include
from views import IndexView, LoanDetailView, ActorDetailView, ActorAddView, LoanAddView, EndorsementAddView

urlpatterns = patterns('',
	url(r'loan/(?P<pk>\d+)$', LoanDetailView.as_view(), name='loan-detail'),
	url(r'actor/(?P<pk>\d+)$', ActorDetailView.as_view(), name='actor-detail'),
	url(r'^actor/create/$',ActorAddView.as_view(),name='actor-add'),
	url(r'^loan/create/$',LoanAddView.as_view(),name='loan-add'),
	url(r'^endorsement/create/$',EndorsementAddView.as_view(),name='endorsement-add'),
    (r'^$', IndexView.as_view()),
)