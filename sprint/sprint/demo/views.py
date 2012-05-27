# Create your views here.

from trust.models import TrustedAgent
from loans.models import LoanModel
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
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
    template_name = 'loan_view.html'
    model = LoanModel

    def get_context_data(self, **kwargs):
        data = super(LoanView, self).get_context_data(**kwargs)
        data['loan'] = data['object']
        return data
        
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super(HomeView, self).get_context_data(**kwargs)
        data['loans'] = LoanModel.objects.all()
        return data
        
