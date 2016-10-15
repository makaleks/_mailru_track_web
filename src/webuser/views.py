from rest_framework import viewsets
from serializers import UserSerializer, WebuserSerializer

from django.contrib.auth.models import User

from models import Webuser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class WebuserViewSet(viewsets.ModelViewSet):
    queryset = Webuser.objects.all()
    serializer_class = WebuserSerializer
