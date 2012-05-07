from neo4django.testutils import *
from graph.models import *
import time

class EvaluationTest(NodeModelTestCase):

    def test_basic_evaluation(self):
        """
        Tests basic evaluation between 2 persons
        """
        p1 = Person.objects.create(first_name="First", last_name="Person")
        p2 = Person.objects.create(first_name="Second", last_name="Person")
        
        e1 = Evaluation.objects.create(type='loan_endorsement', weight=1)
        p1.given_evaluations.add(e1)
        p1.save()
        
        p2.received_evaluations.add(e1)
        p2.save()
        
        p3 = Person.objects.create(first_name="Third", last_name="Person")
        e2 = Evaluation.objects.create(type='loan_endorsement', weight=1, given_by=p3, given_to=p2)
        
    def test_retrive_all_evaluations_for_given_person(self):
        p1 = Person.objects.create(first_name="First", last_name="Person")
        p2 = Person.objects.create(first_name="Second", last_name="Person")
        p3 = Person.objects.create(first_name="Third", last_name="Person")
        
        e1 = LoanEvaluation.objects.create(weight=1, given_by=p1, given_to=p2)
        e2 = LoanEvaluation.objects.create(weight=1, given_by=p3, given_to=p2)
        e3 = LoanEvaluation.objects.create(weight=1, given_by=p1, given_to=p3)
        
        class NannyEvaluation(Evaluation):
            def __init__(self, **kwargs):
                super(NannyEvaluation, self).__init__(**kwargs)
                self.type = "nanny"
        
        e4 = NannyEvaluation.objects.create(weight=-1, given_by=p1, given_to=p2)
        
        evaluations = list(LoanEvaluation.objects.all())
        self.assertEqual(len(evaluations), 3)
        
        for eval in evaluations:
            self.assertEqual(eval.type, LOAN_EVAL_TYPE)
            self.assertEqual(eval.weight, 1)
            
        evaluations = list(NannyEvaluation.objects.all())
        self.assertEqual(len(evaluations), 1)
        
        evaluations = list(p2.received_evaluations.all())
        self.assertEqual(len(evaluations), 3)
        
        # RelationshipQuerySet in neo4django does not support filtering yet :(
        # they mention that this is a todo
        # evaluations = list(p2.received_evaluations.filter(type=LOAN_EVAL_TYPE))
        
        # in the mean time, either iterate manually trough all evaluation and check their type ...
        evaluations = list()
        for eval in p2.received_evaluations.all():
            if (eval.type==LOAN_EVAL_TYPE):
                evaluations.append(eval)
        self.assertEqual(len(evaluations), 2)
        
        # ... or use the filter function
        evaluations = filter(LoanEvaluation.is_instance, p2.received_evaluations.all())
        self.assertEqual(len(evaluations), 2)
        
        