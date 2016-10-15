from webbelonger.views import BelongerViewSet

from serializers import FeedSerializer
from models import Feed


class FeedViewSet(BelongerViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
