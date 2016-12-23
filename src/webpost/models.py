# coding: utf-8
from __future__ import unicode_literals

from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _, ugettext

from webinteractive.models import Interactive

# Create your models here

class Post(Interactive):
    text = models.TextField(default="", verbose_name=_(u'Text'))
    image = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return "post_" + str(self.pk)
    
    class Meta:
        verbose_name = u"Post"
        verbose_name_plural = u"Posts"
        ordering = ('-create_date', )
