# trustscore/api.py
# ============
from tastypie.resources import ModelResource
from models import TrustedAgent

class TrustedAgentResource(ModelResource):
    """docstring for AgentResource"""
    class Meta:
        queryset = TrustedAgent.objects.all()

