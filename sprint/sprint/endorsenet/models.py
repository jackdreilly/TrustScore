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


class Owner(User, AutoPrint):
    
    def new_context(self, space, action_name, person_name):
        context = Context(
            space=space, 
            owner=self, 
            action_name=action_name,
            person_name=person_name
        )
        context.save()
        return context
        
    def space(self):
        try:
            space = self.space_set.all()[0]
        except Exception as e:
            print e
            space = self.create_space()
        finally:
            return space
            
    def create_space(self):
        space = Space(owner=self)
        space.save()
        return space
            
        
    def private_context(self, action_name, person_name):
        return self.new_context(self.space(), action_name, person_name)
        
    def to_string(self):
        return str(self.pk)
        

class Space(models.Model, AutoPrint):
    owner = models.ForeignKey(Owner, related_name='space_owner')
    members = models.ManyToManyField(Owner)
    
    def to_string(self):
        return 'owner: {0}'.format(self.owner)
  
class Context(models.Model, AutoPrint):
    owner = models.ForeignKey(Owner)
    space = models.ForeignKey(Space)
    action_name = models.CharField(max_length=100)
    person_name = models.CharField(max_length=100)

    def to_string(self):
        return '{0} doing {1}'.format(self.person_name, self.action_name)
        
    def new_action(self, person):
        return Action(context=self, person=person)
        
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
    
    context = models.ForeignKey(Context)

    def endorsers(self):
        return [endorsement.endorser for endorsement in self.received_endorsements()]
        
    def received_endorsements(self):
        return self.received_endorsement.all()
        
    def to_string(self):
        return str(self.pk)

class Person(models.Model, AutoPrint):
    owner = models.ForeignKey(Owner)
    
    def to_string(self):
        return '{2} - cxt: {0}, owner: {1}'.format(self.context, self.owner, self.pk)
  
    def give_endorsement(self, subject, score=0):
        return Endorsement(endorser=self, subject=subject, score=score)
    
    def endorsees():
        return [endorsement.subject for endorsement in self.given_endorsements()]
        
    def given_endorsements(self):
        return self.given_endorsement.all()
    
class Endorsement(models.Model, AutoPrint):
    endorser = models.ForeignKey(Person, related_name='given_endorsement')
    subject = models.ForeignKey(Subject, related_name='received_endorsement')
    score = models.FloatField()
    
    def to_string(self):
        return '{0} -> {1}'.format(self.endorser, self.subject)
        
class Action(Subject):
    person = models.ForeignKey(Person)
    
    def to_string(self):
        return 'person: {0}'.format(self.person)
