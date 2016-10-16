from webbelonger.serializers import BelongerSerializer
from models import Album


class AlbumSerializer(BelongerSerializer):
    class Meta:
        model = Album

