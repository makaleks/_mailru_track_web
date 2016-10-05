# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from webbelonger.models import Belonger

# Create your models here.

class Feed(Belonger):
    def __init__(self):
        super().__init__('feed')
    def __unicode__(self):
        return "feed_" + str(self.create_date)
    class Meta:
        verbose_name = u"Лента"
        verbose_name_plural = u"Ленты"
        ordering = ('-create_date', )
