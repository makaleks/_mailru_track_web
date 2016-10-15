from webinteractive.views import InteractiveViewSet

from serializers import PhotoSerializer
from models import Photo


class PhotoViewSet(InteractiveViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
