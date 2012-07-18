from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Subject(models.Model):

    def __repr__(self):
        return str(self.id)

    def __unicode__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()

    def endorsers(self):
        return [endorsement.endorser for endorsement in self.received_endorsements()]
        
    def received_endorsements(self):
        return self.received_endorsement.all()

class Person(Subject):
    def give_endorsement(self, subject, score=0):
        return Endorsement(endorser=self, subject=subject, score=score)
    
    def endorsees():
        return [endorsement.subject for endorsement in self.given_endorsements()]
        
    def given_endorsements(self):
        return self.given_endorsement.all()

    
class Endorsement(models.Model):
    endorser = models.ForeignKey(Person, related_name='given_endorsement')
    subject = models.ForeignKey(Subject, related_name='received_endorsement')
    score = models.FloatField()
    
    def __repr__(self):
        return '{0} -> {1}'.format(self.endorser, self.subject)

    def __unicode__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()


class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def get(cls):
        return cls()
        
    
class EndorseNet(Singleton):
    # this will be the singleton that the algorithm utilizes
    """ note that endorsers may endorse non endorsers (eg loans), this should be accounted for """
    
    def subjects(self):
    	return Subject.objects.all()

    def endorsers_to_depth(self, subject, max_depth = 5):
        depth = 0
        heap = set([subject])
        depths = [[subject]]
        while depth < max_depth:
            depth += 1
            cur = depths[-1]
            next = set()
            depths.append(next)
            for guy in cur:
                endorsers = guy.endorsers()
                next.update(set(endorsers).difference(heap))
                heap.update(endorsers)
        return [(guy, ind) for ind, pack in enumerate(depths) for guy in pack][1:]


def get_network():
	return EndorserNet.get()

