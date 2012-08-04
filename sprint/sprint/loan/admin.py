from django.contrib import admin
from models import Loan, Payment, PaymentMissedEvent, PaymentPaidEvent, LoanDefaultEvent
[
admin.site.register(klass)
for klass in
[Loan, Payment, PaymentMissedEvent, PaymentPaidEvent, LoanDefaultEvent]
]