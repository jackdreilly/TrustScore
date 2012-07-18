from django.contrib import admin
from models import Person, Endorsement, Context, Space, Action, Owner
[
admin.site.register(klass)
for klass in
[Person, Endorsement, Context, Space, Action, Owner]
]

