# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from webbelonger.models import Belonger

# Create your models here.

# Root Feed if used to collect feed objects
# Feed anchors refer to independent RootFeed
# Owners refer to RootFeed
# Using Belonger for Groups allows to get group creator (not owner)

class RootFeed(Belonger):
    def __unicode__(self):
        return "rootfeed_" + str(self.create_date)
    class Meta:
        verbose_name = u"Лентокорень"
        verbose_name_plural = u"Лентокорни"
        ordering = ('-create_date', )

class Feed(models.Model):
    feed_type = models.ForeignKey(ContentType)
    feed_id = models.PositiveIntegerField()
    feed_object = GenericForeignKey('feed_type', 'feed_id')
    create_date = models.DateField(auto_now_add = True)
    def __unicode__(self):
        return "feed_" + str(self.create_date)
    class Meta:
        verbose_name = u"Лента"
        verbose_name_plural = u"Ленты"
        ordering = ('-create_date', )
