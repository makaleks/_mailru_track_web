# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
