# urls.py
# =======
from django.conf.urls.defaults import *
from tastypie.api import Api
from trustscore.api import AgentResource

v1_api = Api(api_name='v1')
v1_api.register(AgentResource())

urlpatterns = patterns('',
    # The normal jazz here then...
    (r'^api/', include(v1_api.urls)),
)