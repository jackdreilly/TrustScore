import datetime
from haystack.indexes import *
from haystack import site
from myapp.models import Note


class PersonIndex(SearchIndex):
	name = CharField(model_attr='name')
	
    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Person.objects.all()


site.register(Note, NoteIndex)