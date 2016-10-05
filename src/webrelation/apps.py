from __future__ import unicode_literals

from django.apps import AppConfig


class WebrelarionConfig(AppConfig):
    name = 'webrelarion'
    def ready(self):
        import signals
