# Create your views here.

from trust.models import TrustedAgent
from django.views.generic.detail import DetailView

class AgentView(DetailView):
    template_name = 'agent.html'
    model = TrustedAgent
    
    def get_context_data(self, **kwargs):
        data = super(AgentView, self).get_context_data(**kwargs)
        agent = data['object'];
        data['endorsements'] = agent.endorsements()
        print data
        return data