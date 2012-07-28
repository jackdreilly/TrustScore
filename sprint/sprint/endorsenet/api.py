from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.conf.urls import url
from tastypie.http import HttpGone, HttpMultipleChoices
from tastypie import fields
from tastypie.utils import trailing_slash
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from endorsenet.models import Space, Context, Subject, Actor, Action, Endorsement, CommitEvent, ActionUpdateEvent
import inflection

class MyModelResource(ModelResource):
	def override_urls(self):
		urls = []
	
		for name, field in self.fields.items():
			if isinstance(field, fields.ToManyField):
				resource = r"^(?P<resource_name>{resource_name})/(?P<{related_name}>.+)/{related_resource}/$".format(
					resource_name = self._meta.resource_name, 
					related_name = field.related_name ,
					related_resource = inflection.singularize(field.attribute),
					)
				print resource
				resource = url(resource, field.to_class().wrap_view('dispatch_list'), name="api_dispatch_detail")
				urls.append(resource)
		return urls

class SpaceResource(MyModelResource):
	"""
	A Space is a container that can hold one or multiple Contexts.
	"""
	class Meta:
		queryset = Space.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()
		fields = ('external_id', 'creator')

	contexts = fields.ToManyField('endorsenet.api.ContextResource', 'contexts', 'space', full = False)

class ContextResource(MyModelResource):
	"""
	A Context holds one instance of an endorsenet and defines meta informations about the nodes of that network.
	"""
	class Meta:
		queryset = Context.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()
		fields = ('external_id', 'creator', 'action_name', 'actor_name')
		filtering = {
			"space": ('exact')
		}

	space = fields.ToOneField('endorsenet.api.SpaceResource', 'space', full = False)
	actors = fields.ToManyField('endorsenet.api.ActorResource', 'actors', 'context', full = False)
	actions = fields.ToManyField('endorsenet.api.ActionResource', 'actions', 'context', full = False)

class SubjectResource(MyModelResource):
	class Meta:
		queryset = Subject.objects.all()

	received_endorsement = fields.ToManyField('endorsenet.api.EndorsementResource', 'received_endorsements', 'subject', full = False)

class ActorResource(SubjectResource):
	"""
	An Actor can be either an endorser (e.g. trustee) or an endorsee (e.g. borrower), or both.
	"""
	class Meta:
		queryset = Actor.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()
		filtering = {
			"context": ('exact')
		}

	context = fields.ToOneField('endorsenet.api.ContextResource', 'context', full = False)
	given_endorsements = fields.ToManyField('endorsenet.api.EndorsementResource', 'given_endorsements', 'endorser', full = False)

class ActionResource(SubjectResource):
	"""
	An Action belongs to an Actor (and endorsee to be more specific) and can be endorsed by other Actors (i.e. endorsees).
	Actions will usually end up with outcomes that then influence the scores in the graph.
	"""
	class Meta:
		queryset = Action.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()
		filtering = {
			"context": ('exact')
		}

	context = fields.ToOneField('endorsenet.api.ContextResource', 'context', full = False)

class EndorsementResource(MyModelResource):
	"""
	An Endorsement is made by an Actor (endorser) to rate a particular subject.  
	A subject can be either another Actor (endorsee) or a particular Action. 
	"""
	
	class Meta:
		queryset = Endorsement.objects.all()
		authorization = Authorization()
		authentication = BasicAuthentication()
		fields = ('external_id', 'subject', 'endorser', 'score')
		filtering = {
			"endorser": ('exact'), 
			"subject": ('exact'),
		}
	
	subject = fields.ToOneField('endorsenet.api.SubjectResource', 'subject', full = False)
	endorser = fields.ToOneField('endorsenet.api.ActorResource', 'endorser', full = False)
