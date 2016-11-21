# coding: utf-8
from __future__ import unicode_literals

from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from webinteractive.models import Interactive

# Create your models here

class Post(Interactive):
    text = models.TextField(default="")
    image = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return "post_" + str(self.pk)

    class Meta:
        verbose_name = u"Пост"
        verbose_name_plural = u"Посты"
        ordering = ('-create_date', )
