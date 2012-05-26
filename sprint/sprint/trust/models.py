from django.db import models
from loans.models import AgentModel
from trust_loaner import loaner
# Create your models here.

class TrustedAgent(AgentModel):
    """docstring for TrustedAgent"""
    trust_score = models.FloatField(default=loaner.good_start)
    
    def __init__(self, *args, **kwargs):
        super(TrustedAgent, self).__init__(*args, **kwargs)