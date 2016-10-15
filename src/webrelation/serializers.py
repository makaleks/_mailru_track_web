from rest_framework import serializers
from models import Friendship


class FriendshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friendship
