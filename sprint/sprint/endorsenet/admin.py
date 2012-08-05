from django.contrib import admin
from models import Endorsement
[
admin.site.register(klass)
for klass in
[Endorsement]
]

