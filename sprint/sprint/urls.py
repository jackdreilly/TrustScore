from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

from django.views.generic.simple import redirect_to


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sprint.views.home', name='home'),
    url(r'^loans/', include('loans.urls')),
    url(r'^demo/', include('demo.urls')),
    url(r'^trust/', include('trust.urls')),
    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', redirect_to, {'url': '/demo/'}),
)
