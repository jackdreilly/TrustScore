from django.db import models
from interfaces.iEndorsement import Endorser, Endorsement
from interfaces.iNetwork import Network as iNetwork


# Create your models here.

class EndorseNode(models.Model, Endorser):
    pass
    
class EndorseEdge(models.Model, Endorsement):
    pass
    
class EndorserNetwork(models.Model, iNetwork):
    """ note that endorsers may endorse non endorsers (eg loans), this should be accounted for """
    pass