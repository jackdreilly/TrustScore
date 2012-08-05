from django.db import models
import sprint.endorsenet.models as e_models
from process_mixin import ProcessAfterSaveMixin
import endorsenet.network
from sprint.auto_print import AutoPrintMixin
import math

class TheTrustScore(object):
    endorse_net = endorsenet.network.get_network()
    DEPTH_FACTOR = .4
    EMENT_SCORE_FACTOR = 1.0

    @classmethod
    def process_trust_event(cls, event):
        action = event.action
        actor = action.actor
        score = event.score
        for subject in (action, actor):
            for endorser, depth in cls.endorse_net.depth_neighbors(subject):
                if not isinstance(endorser, e_models.Actor):
                    continue # endorser is probably the action, no bueno
                cls.generate_trust_propagation(event = event, subject = subject, actor = endorser, depth = depth, score = score)

        
    @classmethod
    def generate_trust_propagation(cls, event, subject, actor, depth, score):
        depth_factor = (cls.DEPTH_FACTOR ** depth)
        ement_factor = cls.EMENT_SCORE_FACTOR * actor.endorsement_score_for_subject(subject)
        prop_score = depth_factor * ement_factor * score
        trust_actor = cls.convert_to_trust_actor(actor)
        prop = TrustPropagation(event = event, score = prop_score, actor = trust_actor)
        prop.save()
        return prop

    @classmethod
    def convert_to_trust_actor(self, actor):
        if isinstance(actor, TrustActor):
            return actor
        return actor.trustactor

    @classmethod
    def process_trust_propagation_event(cls, event):
        actor = event.actor
        actor.trust_score+=event.score
        actor.save()

class TrustActor(e_models.Actor):
    DEFAULT_SCORE = 1.0
    trust_score = models.FloatField(default=DEFAULT_SCORE)

    @property
    def propagations(self):
        return self.trustpropagation_set.order_by('event__date')

    def to_string(self):
        return 'actor: {0}, ts: {1}'.format(self.actor, self.trust_score)


class TrustAction(e_models.Subject):
    actor = models.ForeignKey(TrustActor, related_name='actions')

    def to_string(self):
        return 'actor: {0}'.format(self.actor.to_string())    
    
class TrustEvent(AutoPrintMixin, ProcessAfterSaveMixin, models.Model):
    date = models.DateTimeField(auto_now_add=True)
    action = models.ForeignKey(TrustAction)
    score = models.FloatField()

    def process(self):
        TheTrustScore.process_trust_event(self)

    def to_string(self):
        return 'action: {0}, date: {1}, score: {2}'.format(self.action, self.date, self.score)

class TrustPropagation(AutoPrintMixin, ProcessAfterSaveMixin, models.Model):
    event = models.ForeignKey(TrustEvent)
    score = models.FloatField()
    actor = models.ForeignKey(TrustActor)

    def process(self):
        TheTrustScore.process_trust_propagation_event(self)

    def to_string(self):
        return 'event: {0}, actor: {1}, score: {2}'.format(self.event, self.actor, self.score)
