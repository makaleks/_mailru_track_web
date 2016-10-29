from django.db.models.signals import post_save
from django.contrib.auth.models import User
from models import Webuser

#dispatch_uid="create_user_profile"

def user_post_save(instance, created=False, **kwargs):
    if created:
        webuser = Webuser(user = instance)
        webuser.save()

post_save.connect(user_post_save, User)
