from django.conf.urls import patterns, url, include
from views import IndexView

urlpatterns = patterns('',
    (r'^$', IndexView.as_view()),
)