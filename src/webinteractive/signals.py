from django.db.models.signels import post_save
from .models import Interactive
from webcomment.models import Comment
from webpost.models import Post
from django.utils.cache import caches

cache = caches['default']

def comment_post_save(instance, created=False, **kwargs):
    if created and isinstance(instance.instance, Post):
        cache.set(instance.instance.get_comments_count_cache_key(), None)

post_save.connect(comment_post_save, Comment)
