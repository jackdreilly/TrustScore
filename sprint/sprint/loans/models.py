from django.db import models
from interfaces import iAgent, iNetwork, iLoan
from endorsenet.models import EndorseNode, EndorsableNode
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


class LoanModel(EndorsableNode, iLoan.Loan):
    
    borrower = models.ForeignKey(BorrowerModel, related_name='loan_borrower')
    amount = models.FloatField()
    outcome = models.BooleanField()
    is_active = models.BooleanField()
    funders = models.ManyToManyField(FunderModel, related_name = 'loan_funder',null=True, blank = True)

    def __repr__(self):
        return 'borrower {0}, amount {1}'.format(self.borrower, self.amount)

    def __unicode__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()


    
class AgentModel(BorrowerModel, FunderModel):
    def __repr__(self):
        return '{0}, cs: {1}'.format(self.username, self.credit_score_field)


    def __unicode__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()

    def fund_loan(self, loan):
        loan.funders = self
        loan.save()

    
