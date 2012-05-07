from neo4django.db import models
import neo4django

LOAN_EVAL_TYPE='loan'

class MyStringProperty(models.StringProperty):
    def get_internal_type(self):
        return 'CharField'
        
# the Person node
class Person(models.NodeModel):
    """docstring for Person"""
    first_name = MyStringProperty()
    last_name = MyStringProperty(indexed=True)
    
# ideally this should be a child of models.RelationshipModel
# but that's not supported yet :(
# see https://github.com/scholrly/neo4django/issues/1
# until then, Evaluations are modeled as nodes
# i.e. Person_1 -> Evaluation_A -> Person_2
class Evaluation(models.NodeModel):
    """docstring for Evaluation"""
    type = models.StringProperty(indexed=True)
    weight = models.Property()
    
    given_by = models.Relationship('Person',
                                    rel_type=neo4django.Incoming.GIVEN_BY,
                                    single=True,
                                    related_name='given_evaluations'
                                  )
                                   
    given_to = models.Relationship('Person',
                                    rel_type=neo4django.Outgoing.GIVEN_TO,
                                    single=True,
                                    related_name='received_evaluations'
                                   )

# special type of Evaluation
class LoanEvaluation(Evaluation):
    def __init__(self, **kwargs):
        super(LoanEvaluation, self).__init__(**kwargs)
        self.type = LOAN_EVAL_TYPE
    
    # helper to use for functional filtering
    @staticmethod
    def is_instance(x):
        return isinstance(x, Evaluation) and x.type == LOAN_EVAL_TYPE
        