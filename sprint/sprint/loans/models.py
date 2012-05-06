from django.db import models
from interfaces import iAgent, iNetwork
from referralnetwork.models import Node
# Create your models here.


class BorrowerModel(Node, iAgent.CreditBorrower):
    """ uses credit score """
    credit_score = models.FloatField()
    

class LoanModel(models.Model, iAgent.Loan):
    
    borrower = models.ForeignKey(Node)
    