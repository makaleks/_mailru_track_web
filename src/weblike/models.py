# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from webbelonger.models import Belonger
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Like(Belonger):
    content_type = models.ForeignKey(ContentType)
    content_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'content_id')
    def __unicode__(self):
        return "like_" + str(self.create_date) + "_by_" + self.profile.name.replace(" ", "_")
    class Meta:
        verbose_name = u"Коммент"
        verbose_name_plural = u"Комменты"
        ordering = ('-create_date', )
