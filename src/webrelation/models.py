# coding: utf-8
from __future__ import unicode_literals

from django.db import models

from webuser.models import Webuser
from webbelonger.models import Belonger

# 'Owner will be reciever, because every one can get friendship, but groups can't start it'

class Friendship(Belonger):
    user_from = models.ForeignKey(Webuser, 
                    related_name='friendship_recieve')

    def __unicode__(self):
        return "friendship_" + str(self.pk)

    class Meta:
        verbose_name = u"Дружба"
        verbose_name_plural = u"Дружбы"
        ordering = ('-create_date', )
