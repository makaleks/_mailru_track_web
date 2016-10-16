from webbelonger.views import BelongerViewSet
from serializers import AlbumSerializer
from models import Album


class AlbumViewSet(BelongerViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
