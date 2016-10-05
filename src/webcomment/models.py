# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from webuser.models import Webuser
from webinteractive.models import Interactive

# Create your models here.

class Comment(Interactive):
    text = models.TextField()
    
    content_type = models.ForeignKey(ContentType)
    content_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'content_id')
    def __init__(self):
        super().__init__('comment')
    def __unicode__(self):
        return "comment_" + str(self.create_date) + "_by_" + self.profile.name.replace(" ", "_")
    class Meta:
        verbose_name = u"Коммент"
        verbose_name_plural = u"Комменты"
        ordering = ('-create_date', )
