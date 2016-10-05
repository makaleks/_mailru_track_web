# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from weblike.models import Like
from webbelonger.models import Belonger

# Definition is needed for Comment, because Comment is inherited 
# from Interactive (comment for comment)

class Interactive(Belonger):
    num_comments = models.IntegerField(default = 0)
    num_likes = models.IntegerField(default = 0)
    pass
    class Meta:
        abstract = True

from webcomment.models import Comment

# Create your models here.

class Interactive(Belonger):
    num_comments = models.IntegerField(default = 0)
    num_likes = models.IntegerField(default = 0)
    likes = GenericRelation(Like, content_type_field='content_type',
                object_id_field='content_id')
    comments = GenericRelation(Comment,
                    content_type_field='content_type', 
                    object_id_field='content_id')
    def __init__(self, related_postfix):
        super().__init__(related_postfix)
    class Meta:
        abstract = True

class InteractiveWithName(Interactive):
    name = models.CharField(max_length = 64)
    def __init__(self, related_postfix):
        super().__init__(related_postfix)
    class Meta:
        abstract = True

