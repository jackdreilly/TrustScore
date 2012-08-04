from django.contrib.auth.models import User
from django.db import models

class AutoPrint(object):
    
    def to_string(self):
        return super(AutoPrint, self.__repr__())
        
    def __repr__(self):
        return self.to_string()
    def __str__(self):
        return self.to_string()
    def __unicode__(self):
        return self.to_string()

# created_x = new model, not saved
# saved_x = new model, saved
        

class Space(models.Model, AutoPrint):
    creator = models.ForeignKey(User, related_name='space_creator')
    members = models.ManyToManyField(User)
    
    def to_string(self):
        return 'creator: {0}'.format(self.creator)
  
class Context(models.Model, AutoPrint):
    creator = models.ForeignKey(User)
    space = models.ForeignKey(Space, related_name='contexts')
    action_name = models.CharField(max_length=100)
    actor_name = models.CharField(max_length=100)

    def to_string(self):
        return '{0} doing {1}'.format(self.actor_name, self.action_name)
        
    def subjects(self):
    	return self.subject_set.all()

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
        

class Subject(models.Model, AutoPrint):
    creator = models.ForeignKey(User, null = True, blank = True)
    external_id = models.CharField(max_length=100, null = True, blank = True)
    #context = models.ForeignKey(Context, related_name='actors')

    @property
    def endorsers(self):
        return [endorsement.endorser for endorsement in self.received_endorsements.all()]
        
    def received_endorsements(self):
        return self.received_endorsement.all()
        
    def to_string(self):
        return str(self.pk)

class Actor(Subject, AutoPrint):
    name = models.CharField(max_length = 100, default = 'Anonymous')
    
    def to_string(self):
        return '{1} - creator: {0}'.format(self.creator, self.name)
  
    def give_endorsement(self, subject, score=0):
        return Endorsement(endorser=self, subject=subject, score=score)
    
    @property
    def endorsees():
        return [endorsement.subject for endorsement in self.given_endorsements()]
        
    def given_endorsements(self):
        return self.given_endorsement.all()
    
class Endorsement(models.Model, AutoPrint):
    endorser = models.ForeignKey(Actor, related_name='given_endorsements')
    subject = models.ForeignKey(Subject, related_name='received_endorsements')
    score = models.FloatField(default=1.0)
    
    def to_string(self):
        return '{0} -> {1}: {2}'.format(self.endorser, self.subject, self.score)