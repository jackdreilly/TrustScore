from django.contrib import admin
from models import TrustActor, TrustEvent, TrustPropagation
[
admin.site.register(klass)
for klass in
[TrustActor, TrustEvent, TrustPropagation]
]

