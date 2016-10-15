# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from webbelonger.models import BelongerWithName


class Album(BelongerWithName):
    def __unicode__(self):
        return "album_" + str(self.pk)
    class Meta:
        verbose_name = u"Альбом"
        verbose_name_plural = u"Альбомы"
        ordering = ('-create_date', )
