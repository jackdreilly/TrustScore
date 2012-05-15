# trustscore/api.py
# ============
from tastypie.resources import ModelResource
from models import LoanModel, AgentModel


class LoanResource(ModelResource):
    """docstring for AgentResource"""
    class Meta:
        queryset = LoanModel.objects.all()

class AgentResource(ModelResource):
    """docstring for AgentResource"""
    class Meta:
        queryset = AgentModel.objects.all()

