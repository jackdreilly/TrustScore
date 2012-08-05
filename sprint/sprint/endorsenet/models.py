from django.contrib.auth.models import User
from django.db import models
from sprint.auto_print import AutoPrintMixin

def default_creator():
    try:
        return User.objects.all()[0]
    except IndexError:
        user = User(username='test', email='test@test.com')
        user.save()
        return default_creator()



class Subject(AutoPrintMixin, models.Model):
    creator = models.ForeignKey(User, default = default_creator, blank = True)
    external_id = models.CharField(max_length=100, blank = True, null = True, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True, blank =True)

    def save(self, *args, **kwargs):
        super(Subject, self).save(*args, **kwargs)
        if not self.external_id:
            self.external_id = self.pk
            self.save()

    @property
    def endorsers(self):
        return [endorsement.endorser for endorsement in self.received_endorsements.all()]
        
    def all_received_endorsements(self):
        return self.received_endorsements.all()
        
    def to_string(self):
        return str(self.pk)

    def receive_endorsement_from_actor(self, actor, score):
        ement = Endorsement(endorser = actor, subject = self, score = score)
        ement.save()
        return ement

class Actor(Subject):
    name = models.CharField(max_length = 100, default = 'Anonymous')
    
    def endorsement_score_for_subject(self, subject):
        if self is subject:
            return 1.0
        try:
            gends = self.given_endorsements.filter(subject=subject)
            return gends[0].score
        except IndexError:
            return 0.0

    def to_string(self):
        return '{1} - creator: {0}'.format(self.creator, self.name)
  
    def give_endorsement(self, subject, score=0):
        return Endorsement(endorser=self, subject=subject, score=score)
    
    @property
    def endorsees():
        return [endorsement.subject for endorsement in self.all_given_endorsements()]
        
    def all_given_endorsements(self):
        return self.given_endorsements.all()
    
class Endorsement(AutoPrintMixin, models.Model):
    creator = models.ForeignKey(User, default = default_creator, blank = True)
    date = models.DateTimeField(auto_now_add=True,null=True, blank =True)
    endorser = models.ForeignKey(Actor, related_name='given_endorsements')
    subject = models.ForeignKey(Subject, related_name='received_endorsements')
    score = models.FloatField(default=1.0)
    
    def to_string(self):
        return '{0} -> {1}: {2}'.format(self.endorser, self.subject, self.score)