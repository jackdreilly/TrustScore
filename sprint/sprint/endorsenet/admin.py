from django.contrib import admin
from models import Endorsement, Context, Space, Action, Actor, CommitEvent, ActionUpdateEvent
[
admin.site.register(klass)
for klass in
[Endorsement, Context, Space, Action, Actor, CommitEvent, ActionUpdateEvent]
]

