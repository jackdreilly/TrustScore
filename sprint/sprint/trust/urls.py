# urls.py
# =======
from django.conf.urls.defaults import *
from tastypie.api import Api

urlpatterns = patterns('',
    # The normal jazz here then...
    (r'^api/', include(v1_api.urls)),
)
