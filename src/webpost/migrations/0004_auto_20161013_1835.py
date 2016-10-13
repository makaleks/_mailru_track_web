# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('webpost', '0003_remove_post_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='author_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType'),
            preserve_default=False,
        ),
    ]
