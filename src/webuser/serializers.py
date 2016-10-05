from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers 

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


# Routers provide an easy way of automatically determining the URL conf.
router.register(r'users', UserViewSet)

