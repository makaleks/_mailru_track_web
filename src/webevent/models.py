# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from webbelonger.models import Belonger

# Create your models here.

class Event(Belonger):
    text = models.CharField(max_length = 128)
    event_type = models.ForeignKey(ContentType, null = True)
    event_id = models.PositiveIntegerField()
    event_object = GenericForeignKey('event_type', 'event_id')
    def __init__(self):
        super().__init__('event')
    def __unicode__(self):
        return "event_" + str(self.create_date)
    class Meta:
        verbose_name = u"Событие"
        verbose_name_plural = u"События"
        ordering = ('-create_date', )
