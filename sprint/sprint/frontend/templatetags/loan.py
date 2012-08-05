from django import template
from sprint.loan.models import Loan
Status = Loan.Status
register = template.Library()


@register.inclusion_tag('loan-status-label.html')
def loan_status_label(loan):
    status = loan.status
    if status is Status.ACTIVE:
        text = 'Active'
        klass = 'info'
    elif status is Status.CLOSED:
        text = 'Completed'
        klass = 'success'
    elif status is Status.DEFAULTED:
        text = 'Defaulted'
        klass = 'important'
    return dict(text = text, klass = klass)