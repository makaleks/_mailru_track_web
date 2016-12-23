# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.cache import caches

from webbelonger.models import Belonger

import logging

logger = logging.getLogger(__name__)

cache = caches['default']

class Interactive(Belonger):
    num_comments = models.IntegerField(default = 0, blank = True)
    num_likes = models.IntegerField(default = 0, blank = True)
    # In case of class import - circular import with Comment
    likes = GenericRelation('weblike.Like',
                content_type_field='content_type',
                object_id_field='content_id')
    comments = GenericRelation('webcomment.Comment',
                    content_type_field='content_type', 
                    object_id_field='content_id')
    def get_comments_count_cache_key(self):
        return 'post_{}_comments_count'.format(self.id)
    
    def get_comments_count(self):
        cache_key = self.get_comments_count_cache_key()
        comments_count = cache.get(cache_key)
        if comments_count is None:
            logger.debug('Cached value not found!')
            comments_count = self.comments.all().count()
            cache.set(cache_key, comments_count, 5)
        return comments_count

    class Meta:
        abstract = True

class InteractiveWithName(Interactive):
    name = models.CharField(max_length = 64)
    class Meta:
        abstract = True
