# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from webbelonger.models import BelongerWithName

# Create your models here.

class Chat(BelongerWithName):
    def __init__(self):
        super().__init__('chat')
    def __unicode__(self):
        return "chat_" + str(self.pk)
    class Meta:
        verbose_name = u"Чат"
        verbose_name_plural = u"Чаты"
        ordering = ('-create_date', )
