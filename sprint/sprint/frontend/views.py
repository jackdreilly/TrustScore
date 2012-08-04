from django.views.generic.base import TemplateView
from sprint.loan.models import Loan

class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['loans'] = Loan.objects.all()
        return context