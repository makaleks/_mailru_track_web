# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from webbelonger.models import Belonger


class Interactive(Belonger):
    num_comments = models.IntegerField(default = 0, blank = True)
    num_likes = models.IntegerField(default = 0, blank = True)
    # In case of class import - circular import with Comment
    likes = GenericRelation('weblike.Like',
                content_type_field='content_type',
                object_id_field='content_id')
    comments = GenericRelation('webcomment.Comment',
                    content_type_field='content_type', 
                    object_id_field='content_id')
    class Meta:
        abstract = True

class InteractiveWithName(Interactive):
    name = models.CharField(max_length = 64)
    class Meta:
        abstract = True
