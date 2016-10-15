# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Webprofile(models.Model):
    #avatar = models.ForeignKey('webphoto.Photo', related_name='avatar')
    create_date = models.DateField(auto_now_add = True)
    unread_num = models.IntegerField(default = 0)
    class Meta:
        abstract = True

class Webuser(Webprofile):
    user = models.ForeignKey(User, related_name = 'webprofile')
    # Not in Webprofile because in future it will be stored separately (town, age, relatives...)
    about = models.TextField(default = "", blank = True)
    status = models.CharField(max_length = 64, default = '', blank = True)

    def __unicode__(self):
        return "user" + str(self.pk) + '_' + self.user.username.replace(" ", "_")
    
    class Meta:
        verbose_name = u"Пользователь"
        verbose_name_plural = u"Пользователи"
        ordering = ('-create_date', )

class Webgroup(Webprofile):
    name = models.CharField(max_length = 64)
    about = models.TextField(default = "", blank = True)
    admin = models.ForeignKey(Webuser, related_name = 'owened_group', )
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return "group_" + str(self.pk) + "_" + name.replace(" ", "_")

    class Meta:
        verbose_name = u"Группа"
        verbose_name_plural = u"Группы"
        ordering = ('-create_date', )
