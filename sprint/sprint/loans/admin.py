from django.contrib import admin
from models import BorrowerModel, FunderModel, AgentModel, LoanModel

admin.site.register(BorrowerModel)
admin.site.register(FunderModel)
admin.site.register(AgentModel)
admin.site.register(LoanModel)


