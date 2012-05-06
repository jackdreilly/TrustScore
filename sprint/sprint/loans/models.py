from django.db import models
from interfaces import iAgent, iNetwork, iLoan
from endorsenet.models import EndorseNode
# Create your models here.


class BorrowerModel(EndorseNode, iAgent.CreditBorrower):
    """ uses credit score """
    credit_score_field = models.FloatField()
    
class FunderModel(EndorseNode, iAgent.Funder):
    """ uses credit score """
    
    def will_fund(self, loan):
        # TODO: Implement
        pass


class LoanModel(models.Model, iLoan.Loan):
    
    borrower = models.ForeignKey(BorrowerModel, related_name='loan_borrower')
    amount = models.FloatField()
    endorsers = models.ManyToManyField(EndorseNode)
    outcome = models.BooleanField()
    is_active = models.BooleanField()
    funder = models.ForeignKey(FunderModel, related_name = 'loan_funder')
    
class AgentModel(BorrowerModel, FunderModel):
    pass
    
