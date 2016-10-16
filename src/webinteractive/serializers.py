from rest_framework import serializers
from webbelonger.serializers import BelongerSerializer
from models import Belonger


class InteractiveSerializer(BelongerSerializer):
    num_comments = serializers.ReadOnlyField()
    con_likes = serializers.ReadOnlyField()
