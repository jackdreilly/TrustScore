from django.db import models
from interfaces.iEndorsement import Endorser, Endorsement
from interfaces.iNetwork import Network as iNetwork
from django.contrib.auth.models import User


# Create your models here.

class EndorseNode(User, Endorser):
    pass
    
class EndorseEdge(models.Model, Endorsement):
    pass
    
class EndorserNetwork(iNetwork):
    """ note that endorsers may endorse non endorsers (eg loans), this should be accounted for """
    pass