# urls.py
# =======
from django.conf.urls.defaults import *
from tastypie.api import Api
from api import TrustedAgentResource

v1_api = Api(api_name='v1')
v1_api.register(TrustedAgentResource())

urlpatterns = patterns('',
    # The normal jazz here then...
    (r'^api/', include(v1_api.urls)),
)
