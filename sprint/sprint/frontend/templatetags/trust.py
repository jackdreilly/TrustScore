from django import template
from sprint.trust.models import TrustActor

register = template.Library()

@register.inclusion_tag('trust-history-graph.html')
def trust_history_graph(actor):
    return {'actor': actor}
