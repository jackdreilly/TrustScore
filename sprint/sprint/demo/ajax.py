from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from trust.models import TrustedAgent

@dajaxice_register
def endorser_trust_scores(request, pk):
    agent = TrustedAgent.objects.get(pk=pk)
    endorsements = agent.endorsements()
    print dir(endorsements[0])
    return simplejson.dumps({
        'endorsers': [
            {
                'name': end.endorse_this.first_name,
                'trust_score': end.endorse_this.borrowermodel.agentmodel.trustedagent.trust_score,
                'score': end.score
            } for end in endorsements
        ]
    }
    )
    