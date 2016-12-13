from rest_framework import viewsets
from serializers import UserSerializer, WebuserSerializer

from django.contrib.auth.models import User

from models import Webuser

from .permissions import ReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (ReadOnly, )
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class WebuserViewSet(viewsets.ModelViewSet):
    permission_classes = (ReadOnly, )
    queryset = Webuser.objects.all()
    serializer_class = WebuserSerializer
