from webbelonger.views import BelongerViewSet

from serializers import FriendshipSerializer
from models import Friendship


class FriendshipViewSet(BelongerViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
