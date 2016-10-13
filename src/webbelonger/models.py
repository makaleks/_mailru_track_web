from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from webuser.models import Webprofile

# Create your models here.

class Belonger(models.Model):
    author_type = models.ForeignKey(ContentType, 
            related_name = '+')
    author_id = models.PositiveIntegerField()
    author_object = GenericForeignKey('author_type', 'author_id')
    #def __init__(self, related_postfix):
    '''self.author_type = models.ForeignKey(ContentType, 
            related_name = '+author_type_' + related_postfix)
        self.author_id = models.PositiveIntegerField()
        self.author_object = GenericForeignKey('author_type', 'author_id')
    '''
    create_date = models.DateField(auto_now_add = True)
    class Meta:
        abstract = True

class BelongerWithName(Belonger):
    name = models.CharField(max_length = 64)
    '''def __init__(self, related_postfix):
        super().__init__(related_postfix)'''
    class Meta:
        abstract = True
