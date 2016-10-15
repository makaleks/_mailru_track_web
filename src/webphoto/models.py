# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from webinteractive.models import InteractiveWithName
from webalbum.models import Album

# Create your models here.

class Photo(InteractiveWithName):
    data = models.ImageField()
    album = models.ForeignKey('webalbum.Album', related_name = 'photos')
    def __unicode__(self):
        return "IMG_" + str(self.pk)
    class Meta:
        verbose_name = u"Картинка"
        verbose_name_plural = u"Картинки"
        ordering = ('-create_date', )
