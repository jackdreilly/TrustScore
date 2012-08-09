from django.forms import ModelForm, ModelChoiceField
from sprint.endorsenet.models import Endorsement
from sprint.trust.models import TrustActor
from sprint.loan.models import Loan

class BorrowerEndorsementForm(ModelForm):
    class Meta:
        model = Endorsement
    subject = ModelChoiceField(queryset=TrustActor.objects.all())

class LoanEndorsementForm(ModelForm):
    class Meta:
        model = Endorsement
    subject = ModelChoiceField(queryset=Loan.objects.all())