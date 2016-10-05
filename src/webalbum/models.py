# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from webbelonger.models import BelongerWithName

# Create your models here.

class Album(BelongerWithName):
    name = models.CharField(max_length = 64)
    def __init__(self):
        super().__init__('album')
    def __unicode__(self):
        return "ALBUM_" + str(self.pk)
    class Meta:
        verbose_name = u"Альбом"
        verbose_name_plural = u"Альбомы"
        ordering = ('-create_date', )
