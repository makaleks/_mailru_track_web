# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from webuser.models import Webuser
from webbelonger.models import Belonger

# Create your models here.

# 'Owner will be reciever, because every one can get friendship, but groups can't start it'
class Friendship(Belonger):
    user_from = models.ForeignKey('webuser.Webuser', related_name='friendship_recieve')
    def __unicode__(self):
        return "friendship_" + str(self.create_date)
    class Meta:
        verbose_name = u"Дружба"
        verbose_name_plural = u"Дружбы"
        ordering = ('-create_date', )
