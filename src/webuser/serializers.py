from rest_framework import serializers
from django.contrib.auth.models import User

from models import Webuser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        #lookup_field = 'username'
        fields = ('url', 'username', 'email')

class WebuserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Webuser
        fields = ('user', 'about', 'status')
