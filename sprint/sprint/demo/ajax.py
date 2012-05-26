from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from trust.models import TrustedAgent

@dajaxice_register
def endorser_trust_scores(request, pk):
    print 'got here'
    agent = TrustedAgent.objects.get(pk=pk)
    print 'agent', agent
    endorsers = [endr.borrowermodel.agentmodel.trustedagent for endr in agent.endorsers()]
    return simplejson.dumps({
        'endorsers': [
            {
                'name': endr.first_name,
                'trust_score': endr.trust_score
            } for endr in endorsers
        ]
    }
    )