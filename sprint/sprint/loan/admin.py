from django.contrib import admin
from models import Loan, Payment, PaymentMissedEvent, PaymentPaidEvent, LoanDefaultEvent, PaymentTrustEvent
[
admin.site.register(klass)
for klass in
[Loan, Payment, PaymentMissedEvent, PaymentPaidEvent, LoanDefaultEvent, PaymentTrustEvent]
]