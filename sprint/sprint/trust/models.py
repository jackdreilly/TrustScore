from django.contrib.auth.models import User
from django.db import models
from endorsenet import models as en_models

class AutoPrint(object):
    
    def to_string(self):
        return super(AutoPrint, self.__repr__())
        
    def __repr__(self):
        return self.to_string()
    def __str__(self):
        return self.to_string()
    def __unicode__(self):
        return self.to_string()

# created_x = new model, not saved
# saved_x = new model, saved

class TrustContext(models.Model, AutoPrint):
    context = models.ForeignKey(en_models.Context)
    forgiveness = models.FloatField(default=1.0)
    