from django.db import models
from interfaces.iEndorsement import Endorser, ScoreEndorsement
from interfaces.iNetwork import Network as iNetwork
from django.contrib.auth.models import User


# Create your models here.

class EndorsableNode(models.Model):

    def __repr__(self):
        return str(self.id)


    def __unicode__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()

    def endorsers(self):
        return [end.endorse_this for end in self.endorse_that.all()]
        
    def endorsements(self):
        return self.endorse_that.all()



class EndorseNode(User, EndorsableNode, Endorser):
    # here I have assumed that any endorser must have a full account
    def __init__(self, *args, **kwargs):
        super(EndorseNode, self).__init__(*args, **kwargs)

    def endorsement(self, endorsable, score=0):
        return EndorseEdge(endorser=self, endorsee=endorsable, score=score)

    
class EndorseEdge(models.Model, ScoreEndorsement):
    # I do not use this yet, but something should inherit the Endorsement interface
    endorse_this = models.ForeignKey(EndorseNode, related_name='endorse_this')
    endorse_that = models.ForeignKey(EndorsableNode, related_name='endorse_that')
    score = models.FloatField()
    
    def __init__(self,*args,**kwargs):
    	if len(kwargs) is 0:
    		models.Model.__init__(self, *args,**kwargs)
    		return
    	endorser = kwargs.pop('endorser')
    	endorsee = kwargs.pop('endorsee')
    	score = kwargs['score']
    	
    	ScoreEndorsement.__init__(self, score=score, endorsee=endorsee, endorser=endorser)
    	
    	kwargs['endorse_this'] = endorser
    	kwargs['endorse_that'] = endorsee
    	
    	print(kwargs)
    	
    	models.Model.__init__(self, *args,**kwargs)

    def __repr__(self):
        return 'endr: {0}, endee: {1}'.format(self.endorse_this, self.endorse_that)


    def __unicode__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()


    
class EndorserNetwork(iNetwork):
    # this will be the singleton that the algorithm utilizes
    """ note that endorsers may endorse non endorsers (eg loans), this should be accounted for """
    
    def neighbors(self, node):
    	return [endorsement.endorse_that.endorsenode 
            for endorsement in node.endorse_this.all() 
            if hasattr(endorsement.endorse_that, 'endorsenode')]

    def nodes(self):
    	return EndorseNode.objects.all()

    def bfs_iterator(self, node, max_depth = 5):
        depth = 0
        heap = set([node])
        depths = [[node]]
        while depth < max_depth:
            depth += 1
            cur = depths[-1]
            next = set()
            depths.append(next)
            print 'checking cur'
            for guy in cur:
                print 'checking guy', guy
                endorsers = guy.endorsers()
                print 'guy endorsers', endorsers
                next.update(set(endorsers).difference(heap))
                print 'next', next
                heap.update(endorsers)
                print 'heap', heap
        return [(guy, ind) for ind, pack in enumerate(depths) for guy in pack]








def get_network():
	return EndorserNetwork.get()

