from webbelonger.serializers import BelongerSerializer
from models import Message


class MessageSerializer(BelongerSerializer):
    class Meta:
        model = Message
