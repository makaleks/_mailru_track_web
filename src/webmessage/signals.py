from django.db.models.signals import post_save
from .models import Message
from webuser.tasks import send_email_notification

#dispatch_uid="create_user_profile"

def messages_post_save(instance, created=False, **kwargs):
    if created:
        send_email_notification.delay("makaleks@live.ru", 'Celery task', 'Alive task.')

post_save.connect(messages_post_save, Message)
