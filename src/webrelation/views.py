from models import Friendship
from rest_framework import viewsets
from serializers import FriendshipSerializer

# ViewSets define the view behavior.
class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
