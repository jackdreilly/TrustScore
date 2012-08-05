from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from sprint.loan.models import Loan
from sprint.trust.models import TrustActor
from sprint.endorsenet.models import Endorsement

class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        loans =Loan.objects.all()
        active_loans = [loan for loan in loans if loan.status is Loan.Status.ACTIVE]
        context['loans'] = loans
        context['active_loans'] = active_loans
        actors = TrustActor.objects.all()
        for actor in actors:
            actor.loans = Loan.get_loans_for_actor(actor)
        context['actors'] = actors
        context['actor_add_view'] = ActorAddView.as_view()(self.request).render().rendered_content
        context['loan_add_view'] = LoanAddView.as_view()(self.request).render().rendered_content
        context['endorsement_add_view'] = EndorsementAddView.as_view()(self.request).render().rendered_content
        return context


class LoanDetailView(DetailView):
    context_object_name = "loan"
    template_name = "loan-detail.html"
    model = Loan


class ActorDetailView(DetailView):
    context_object_name = "actor"
    template_name = "actor-detail.html"
    model = TrustActor


class ActorAddView(CreateView):
    template_name = "add-borrower-form.html"
    model = TrustActor
    success_url = "/"

class LoanAddView(CreateView):
    template_name = "add-loan-form.html"
    model = Loan
    success_url = "/"

class EndorsementAddView(CreateView):
    template_name = "add-endorsement-form.html"
    model = Endorsement
    success_url = "/"