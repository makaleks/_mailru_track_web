# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from webbelonger.models import Belonger


class Like(Belonger):
    content_type = models.ForeignKey(ContentType)
    content_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'content_id')

    def __unicode__(self):
        return "like_" + str(self.pk)
    
    class Meta:
        verbose_name = u"Лайк"
        verbose_name_plural = u"Лайки"
        ordering = ('-create_date', )
