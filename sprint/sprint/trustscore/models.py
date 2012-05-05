from django.db import models
from django.contrib.auth.models import User
import interfaces.itrust

# Create your models here.

class Agent(models.Model):
    """docstring for Agent"""
    user = models.ForeignKey(User)


