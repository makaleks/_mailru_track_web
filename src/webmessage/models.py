# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from webbelonger.models import Belonger
from webchat.models import Chat

# Create your models here.

class Message(Belonger):
    text = models.TextField(default="")
    chat = models.ForeignKey(Chat, related_name = 'messages')
    def __unicode__(self):
        return "message_" + str(self.create_date)
    class Meta:
        verbose_name = u"Сообщение"
        verbose_name_plural = u"Сообщения"
        ordering = ('-create_date', )
