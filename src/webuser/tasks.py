from celery.task import task, periodic_task
from django.core.mail import send_mail


@task
def add(x, y):
    return x + y

@task
def send_email_notification(to, subject, text):
    send_mail(subject, text, 'idenxxx@mail.ru', [to], fail_silently=False)

# run_every - second
@periodic_task(run_every=3600*24)
def send_email_notification(to, subject, text):
    send_mail(subject, text, 'idenxxx@mail.ru', [to], fail_silently=False)