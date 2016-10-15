# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User

# Create your models here.

class Webprofile(models.Model):
    #avatar = models.ForeignKey('webphoto.Photo', related_name='avatar')
    create_date = models.DateField(auto_now_add = True)
    unread_num = models.IntegerField(default = 0)

    class Meta:
        abstract = True

class Webuser(Webprofile):
    user = models.ForeignKey(User, related_name = 'webprofile')
    # Not in Webprofile because in future it will be stored separately (town, age, relatives...)
    about = models.TextField(default = "")
    status = models.CharField(max_length = 64, default = '')
    def __unicode__(self):
        return "user_" + str(self.pk) + name.replace(" ", "_")
    class Meta:
        verbose_name = u"Пользователь"
        verbose_name_plural = u"Пользователи"
        ordering = ('-create_date', )

class Webgroup(Webprofile):
    name = models.CharField(max_length = 64)
    about = models.TextField(default = "")
    admin = models.ForeignKey(Webuser, related_name = 'owened_group', )
    users = models.ManyToManyField(User)
    def __unicode__(self):
        return "group_" + str(self.pk) + "_" + name.replace(" ", "_")
    class Meta:
        verbose_name = u"Группа"
        verbose_name_plural = u"Группы"
        ordering = ('-create_date', )
