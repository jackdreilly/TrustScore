from django.db import models
import sprint.endorsenet.models as e_models

class TrustActor(e_models.Actor):
    DEFAULT_SCORE = 1.0
    trust_score = models.FloatField(default=DEFAULT_SCORE)

class TrustAction(e_models.Subject):
	creation_date = models.DateTimeField(auto_now_add=True)
    actor = models.ForeignKey(TrustActor, related_name='actions')
    
class TrustEvent(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    action = models.ForeignKey(TrustAction)
    score = models.FloatField()