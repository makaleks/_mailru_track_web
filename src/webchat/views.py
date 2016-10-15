from webbelonger.views import BelongerViewSet

from serializers import ChatSerializer
from models import Chat


class ChatViewSet(BelongerViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
