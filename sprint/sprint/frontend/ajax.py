from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from sprint.trust.models import TrustActor

def cum_sum(lst):
    new_lst = [lst[0]]
    for next in lst[1:]:
        new_lst.append(next + new_lst[-1])
    return new_lst


class TrustHistory(object):

    def __init__(self, actor):
        self.actor = actor
        self.propagations = actor.propagations
        self.start = actor.DEFAULT_SCORE
        self.start_date = actor.creation_date
        self.y_points = cum_sum([self.start] + [prop.score for prop in self.propagations])
        self.t_points = [0] + [
            (prop.event.date - self.start_date).total_seconds()
            for prop in self.propagations
        ]

    def to_jsonable(self):
    	return {
    		'actor': self.actor.name,
    		'propagations': [
    			{
    				'event': prop.event.pk,
    				'actor': prop.event.action.actor.name
    			}
    			for prop in self.propagations
    		],
    		'y_points', self.y_points,
    		't_points', self.t_points
    	}


@dajaxice_register
def trust_history(request, actor_pk):
	actor = TrustActor.objects.get(pk=actor_pk)
    return simplejson.dumps(TrustHistory(actor).to_jsonable())