from __future__ import unicode_literals

from django.apps import AppConfig


class WebfeedConfig(AppConfig):
    name = 'webfeed'
    def ready(self):
        import signals
