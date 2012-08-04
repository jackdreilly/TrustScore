from django.db import models
import sprint.endorsenet.models as e_models

class TrustActor(e_models.Actor):
    DEFAULT_SCORE = 1.0
    trust_score = models.FloatField(default=DEFAULT_SCORE)

class Action(e_models.Subject):
    actor = models.ForeignKey(TrustActor)
    
class TrustEvent(models.Model):
    date = models.DateTimeField()
    action = models.ForeignKey(Action)
    score = models.FloatField()