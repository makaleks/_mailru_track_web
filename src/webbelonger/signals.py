from django.db.models.signals import post_save

def belonger_post_save(instance, ... created=False):
    if created:
        instance.obj.author_object.unread_num += 1

post_save.connect(comment_post_save, Belonger)
