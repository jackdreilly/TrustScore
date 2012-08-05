from django import template
from sprint.trust.models import TrustActor

register = template.Library()

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

@register.inclusion_tag('trust-history-graph.html')
def trust_history_graph(actor):
    return {'history': TrustHistory(actor)}
