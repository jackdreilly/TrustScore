# trustscore/api.py
# ============
from tastypie.resources import ModelResource
from trustscore.models import Agent


class AgentResource(ModelResource):
    """docstring for AgentResource"""
    class Meta:
        queryset = Agent.objects.all() 