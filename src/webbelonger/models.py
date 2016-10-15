from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from webuser.models import Webuser

# Create your models here.

class Belonger(models.Model):
    owner = models.ForeignKey(Webuser, related_name = '%(class)s_creature')
    create_date = models.DateField(auto_now_add = True)
    edit_date = models.DateField(auto_now_add = True)
    class Meta:
        abstract = True

class BelongerWithName(Belonger):
    name = models.CharField(max_length = 64)
    class Meta:
        abstract = True
