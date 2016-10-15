from webbelonger.views import BelongerViewSet

from serializers import MessageSerializer
from models import Message


class MessageViewSet(BelongerViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
