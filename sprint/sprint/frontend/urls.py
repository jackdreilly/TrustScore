from django.conf.urls import patterns, url, include
from views import IndexView, LoanDetailView, ActorDetailView, ActorAddView, LoanAddView, LoanEndorsementAddView, BorrowerEndorsementAddView, ActorsView, LoansView

urlpatterns = patterns('',
	url(r'loan/(?P<pk>\d+)$', LoanDetailView.as_view(), name='loan-detail'),
	url(r'actor/(?P<pk>\d+)$', ActorDetailView.as_view(), name='actor-detail'),
	url(r'^actor/create/$',ActorAddView.as_view(),name='actor-add'),
	url(r'^loan/create/$',LoanAddView.as_view(),name='loan-add'),
	url(r'^borrower-endorsement/create/$',BorrowerEndorsementAddView.as_view(),name='borrower-endorsement-add'),
	url(r'^loan-endorsement/create/$',LoanEndorsementAddView.as_view(),name='loan-endorsement-add'),
    url(r'^actors$', ActorsView.as_view(), name='actors'),
    url(r'^loans$', LoansView.as_view(), name='loans'),
    url(r'^$', IndexView.as_view(),name='index'),

)