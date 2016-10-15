from webbelonger.views import BelongerViewSet

from serializers import LikeSerializer
from models import Like


class LikeViewSet(BelongerViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
