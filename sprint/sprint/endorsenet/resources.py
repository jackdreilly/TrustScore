from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource
from endorsenet.models import Space, Context, Actor, Action, Endorsement, CommitEvent, ActionUpdateEvent

class SpaceResource(ModelResource):
	"""
	A Space is a container that can hold one or multiple Contexts.
	"""
	model = Space

	def contexts(self, instance):
		return reverse('contexts', kwargs={'space': instance.key})


class ContextResource(ModelResource):
	"""
	A Context holds one instance of an endorsenet and defines meta informations about the nodes of that network.
	"""
	model = Context
	fields = ('action_name', 'actor_name')
	
	def space(self, instance):
		return reverse('space', kwargs={'key': instance.space.key})

	def actors(self, instance):
		return reverse('actors', kwargs={'context': instance.key})

	def actions(self, instance):
		return reverse('actions', kwargs={'context': instance.key})

	def endorsements(self, instance):
		return reverse('endorsements', kwargs={'context': instance.key})


class ActorResource(ModelResource):
	"""
	An Actor can be either an endorser (e.g. trustee) or an endorsee (e.g. borrower), or both.
	"""
	model = Actor
	fields = ('external_id')

	def context(self, instance):
		return reverse('context', kwargs={'key': instance.context.key})

class ActionResource(ModelResource):
	"""
	An Action belongs to an Actor (and endorsee to be more specific) and can be endorsed by other Actors (i.e. endorsees).
	Actions will usually end up with outcomes that then influence the scores in the graph.
	"""
	model = Action
	fields = ('external_id', 'context', 'actor')

	def context(self, instance):
		return reverse('context', kwargs={'key': instance.context.key})

class EndorsementResource(ModelResource):
	"""
	An Endorsement is made by an Actor (endorser) to rate a particular subject.  
	A subject can be either another Actor (endorsee) or a particular Action. 
	"""
	model = Endorsement
	fields = ('external_id', 'subject', 'endorser', 'score')

	def context(self, instance):
		return reverse('context', kwargs={'key': instance.context.key})

