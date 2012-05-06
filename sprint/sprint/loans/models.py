from django.db import models
from interfaces import iAgent, iNetwork, iLoan
from endorsenet.models import EndorseNode
# Create your models here.


class BorrowerModel(EndorseNode, iAgent.CreditBorrower):
    """ uses credit score """
    # subclasses the EndorseNode, which means it can participate in network, 
    # additionally is assumed to have external information in the form of a credit score
    credit_score_field = models.FloatField()
    
class FunderModel(EndorseNode, iAgent.Funder):
    # These special case classes are important for generalization down the road
    # as can be seen in LoanModel, each node need only be endowed with certain properties
    # specific to funding and borrowing.
    # of course, this can be superceded by implementing every EndorseNode as an AgentModel,
    # since it inherits from all special cases.
    
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
    
