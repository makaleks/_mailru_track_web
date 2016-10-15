# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from webinteractive.models import Interactive


class Comment(Interactive):
    text = models.TextField()
    
    content_type = models.ForeignKey(ContentType,
            related_name='content_type')
    content_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'content_id')

    def __unicode__(self):
        return "comment_" + str(self.pk)

    class Meta:
        verbose_name = u"Коммент"
        verbose_name_plural = u"Комменты"
        ordering = ('-create_date', )
