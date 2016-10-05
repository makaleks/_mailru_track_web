from __future__ import unicode_literals

from django.apps import AppConfig


class WebmessageConfig(AppConfig):
    name = 'webmessage'
    def ready(self):
        import signals
