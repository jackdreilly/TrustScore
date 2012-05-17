# Create your views here.

from loans.models import AgentModel
from django.views.generic.detail import DetailView

class AgentView(DetailView):
    template_name = 'agent.html'
    model = AgentModel
    
    def get_context_data(self, **kwargs):
        data = super(AgentView, self).get_context_data(**kwargs)
        agent = data['object'];
        data['endorsements'] = agent.endorsements()
        print data
        return data
    