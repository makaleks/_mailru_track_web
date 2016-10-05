from django.db.models.signals import post_save
from models import Like

def like_post_save(instance, ... created=False):
    if created:
        instance.obj.content_object.num_likes += 1


post_save.connect(like_post_save, Like)
