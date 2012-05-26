# Create your views here.

from trust.models import TrustedAgent
from loans.models import LoanModel
from django.views.generic.detail import DetailView

class AgentView(DetailView):
    template_name = 'agent.html'
    model = TrustedAgent
    
    def get_context_data(self, **kwargs):
        data = super(AgentView, self).get_context_data(**kwargs)
        agent = data['object'];
        data['endorsements'] = agent.endorsements()
        data['loans'] = agent.loans()
        data['agent'] = agent
        del data['object']
        return data
        

class LoanView(DetailView):
    template_name = 'loan.html'
    model = LoanModel
    
    def get_context_data(self, **kwargs):
        loan = super(LoanView, self).get_context_data(**kwargs)