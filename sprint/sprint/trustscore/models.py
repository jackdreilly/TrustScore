from django.db import models
from django.contrib.auth.models import User
import interfaces.itrust

# Create your models here.

class Agent(models.Model):
    # this is completely bogus and should be deleted
    """docstring for Agent"""
    user = models.ForeignKey(User)


