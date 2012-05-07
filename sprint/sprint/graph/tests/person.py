from neo4django.testutils import *
from graph.models import Person
import time

class PersonTest(NodeModelTestCase):

    def test_create_person(self):
        """
        Tests creation of a new person node
        """
        p = Person(first_name="Foo", last_name="Bar")
        self.assertIsNone(p.id)
        p.save()
        self.assertIsNotNone(p.id)

    def test_retrieve_person_by_id(self):
        """
        Tests retrieval of one person node by id
        """
        p1 = Person(first_name="Foo", last_name="Bar")
        p1.save()
        
        p2 = Person(first_name="Bar", last_name="Foo")
        p2.save()
        
        p3 = Person.objects.get(id=p1.id)
        
        self.assertEqual(p1.id, p3.id)
        self.assertEqual(p1.first_name, p3.first_name)
        self.assertEqual(p1.last_name, p3.last_name)
        
        self.assertNotEqual(p2.id, p3.id)
        self.assertNotEqual(p2.first_name, p3.first_name)
        self.assertNotEqual(p2.last_name, p3.last_name)

    def test_retrieve_all_persons(self):
        """
        Tests retrieval of all person nodes
        """
        p1 = Person(first_name="Foo", last_name="Bar")
        p1.save()
        
        p2 = Person(first_name="Bar", last_name="Foo")
        p2.save()
        
        persons = Person.objects.all()
        self.assertEqual(len(persons), 2)


    def test_retrieve_filter_persons(self):
        """
        Tests filtering of person nodes
        """
        p1 = Person(first_name="Foo", last_name="Bar")
        p1.save()

        p2 = Person(first_name="Foo", last_name="Bar")
        p2.save()

        p3 = Person(first_name="Bar", last_name="Foo")
        p3.save()

        persons = Person.objects.filter(last_name="Bar")
        self.assertEqual(len(persons), 2)