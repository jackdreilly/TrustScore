from django.db import models
from interfaces.iEndorsement import Endorser, Endorsement
from interfaces.iNetwork import Network as iNetwork
from django.contrib.auth.models import User


# Create your models here.

class EndorseNode(User, Endorser):
    # here I have assumed that any endorser must have a full account
    pass
    
class EndorseEdge(models.Model, Endorsement):
    # I do not use this yet, but something should inherit the Endorsement interface
    pass
    
class EndorserNetwork(iNetwork):
    # this will be the singleton that the algorithm utilizes
    """ note that endorsers may endorse non endorsers (eg loans), this should be accounted for """
    pass