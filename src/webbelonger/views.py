from rest_framework import viewsets, permissions
from serializers import BelongerSerializer

from webuser.models import Webuser

from rest_framework import permissions

from models import Belonger
from permissions import IsOwnerOrReadOnly

from oauth2_provider.models import AccessToken, get_application_model
from rest_framework.authtoken.models import Token

# Belonger is Meta, so 'with_name' version will appear in the end serializers

class BelongerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    
    def perform_create(self, serializer):
        uprofile = Webuser.objects.get(user=self.request.user)
        serializer.save(owner = uprofile)

    def get_queryset(self):
        qs = super(BelongerViewSet, self).get_queryset()
        if self.request.query_params.get('username'):
            qs = qs.filter(owner__user__username = 
                    self.request.query_params.get('username'))
        if self.request.query_params.get('create_date'):
            qs = qs.filter(create_date =
                    self.request.query_params.get('create_date'))
        return qs
