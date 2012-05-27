from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from trust_loaner import loaner
from loans.models import LoanModel

@dajaxice_register
def trust_stats(request, loan_pk):
    loan = LoanModel.objects.get(pk=loan_pk)
    cs, e_scores, e_score, tot_score = loaner.loan_stats(loan)
    thresh = loaner.fund_threshold
    return simplejson.dumps({
        'cs': cs,
        'e_scores': e_scores,
        'e_score': e_score,
        'tot_score': tot_score,
        'threshold': thresh
    })