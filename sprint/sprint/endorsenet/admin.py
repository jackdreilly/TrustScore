from django.contrib import admin
from models import Endorsement, Context, Space, Subject, Actor
[
admin.site.register(klass)
for klass in
[Endorsement, Context, Space]
]

