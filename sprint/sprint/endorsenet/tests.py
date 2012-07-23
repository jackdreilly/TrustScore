"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import unittest
from django.db import IntegrityError
from django.test import TestCase
from endorsenet.models import Subject
from endorsenet.models import Owner
from endorsenet.models import Context


class OwnerTest(TestCase, unittest.TestCase):

    def test_create_owner(self):
        owner = Owner()
        self.assertEquals(owner.pk, None)
        owner.save()
        self.assertNotEquals(owner.pk, None)

    def test_create_space(self):
        owner = Owner()
        self.assertRaises(IntegrityError, lambda: owner.create_space())

        owner.save()
        space = owner.create_space()
        self.assertNotEquals(space.pk, None)
        

    def test_new_context(self):
        owner = Owner()
        owner.save()
        space = owner.create_space();
        context = owner.new_context(space, "Action", "Person")
        self.assertNotEquals(context.pk, None)
        self.assertEquals(context.action_name, "Action")
        self.assertEquals(context.person_name, "Person")
        self.assertEquals(context.space, space)

class SubjectTest(TestCase, unittest.TestCase):
    
    def new_owner(self):
        owner = Owner()
        owner.save()
        return owner

    def test_create_subject(self):
        """
        Tests creation of Subject
        """
        subject = Subject()

        # no endorsers right after creation
        self.assertEquals(subject.endorsers(), [])

        # context not yet set
        # @todo: should probably add context as param to subject 
        #        constructor or make context a factory for subjects
        self.assertRaises(Context.DoesNotExist, lambda: subject.context)
        self.assertRaises(IntegrityError, lambda: subject.save());

        
        # set context and try save again
        owner = self.new_owner()
        subject.context = owner.new_context(owner.create_space(), "Action", "Person")
        subject.save()

        self.assertNotEquals(subject.pk, None);