from django.db.models.signals import post_save
from models import Comment

def comment_post_save(instance, ... created=False):
    if created:
        instance.obj.content_object.num_comments += 1


post_save.connect(comment_post_save, Comment)
