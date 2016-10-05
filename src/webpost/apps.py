from __future__ import unicode_literals

from django.apps import AppConfig


class WebpostConfig(AppConfig):
    name = 'webpost'
    def ready(self):
        import signals
