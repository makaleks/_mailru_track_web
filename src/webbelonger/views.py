from rest_framework import viewsets
from serializers import BelongerSerializer

from webuser.models import Webuser

from models import Belonger

# Belonger is Meta, so 'with_name' version will appear in the end serializers

class BelongerViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        user = relf.request.user
        profile = Webuser.objects.get(webprofile=user)
        serializer.save(author=profile)
