"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import unittest
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase
from endorsenet.models import Subject, Endorsement, Actor


class NewSubject(TestCase, unittest.TestCase):

    def test_create_new_subject(self):
        subject = Subject()
        subject.save()

    @classmethod
    def create_new_subject_w_ex_id(cls, ex_id):
        subject = Subject(external_id = ex_id)
        subject.save()
        return subject

    def test_duplicate_ex_id(self):
        ex_id = 30
        subject = Subject(external_id = ex_id)
        subject.save()
        subject = Subject(external_id = ex_id)
        self.assertRaises(IntegrityError, lambda: subject.save())


class NewActor(TestCase, unittest.TestCase):

    @classmethod
    def create_actor(cls, name):
        actor = Actor(name=name)
        actor.save()
        return actor

    def test_create_actor(self):
        self.create_actor('jack')
        self.create_actor('john')


class NewEndorsement(TestCase, unittest.TestCase):

    @classmethod
    def create_endorsement(self, actor, subject, score):
        ement = Endorsement(endorser=actor, subject=subject, score=score)
        ement.save()
        return ement

    def test_create_endorsement(self):
        actor = NewActor.create_actor('actor')
        subject = NewSubject.create_new_subject_w_ex_id(42)
        score = 10.0
        self.create_endorsement(actor, subject, score)
        
    def test_bad_endorsement(self):
        actor = NewActor.create_actor('actor')
        subject = NewSubject.create_new_subject_w_ex_id(42)
        score = 10.0
        self.assertRaises(ValueError, lambda: self.create_endorsement(subject, subject, score))