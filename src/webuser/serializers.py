from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        #lookup_field = 'username'
        fields = ('url', 'username', 'email')
