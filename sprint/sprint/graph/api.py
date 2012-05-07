from djangorestframework.resources import ModelResource
from graph.models import *

class PersonResource(ModelResource):
    model = Person
    
class EvaluationResource(ModelResource):
    model = LoanEvaluation