from __future__ import unicode_literals

from django.apps import AppConfig


class WebphotoConfig(AppConfig):
    name = 'webphoto'
    def ready(self):
        import signals
