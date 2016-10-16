from rest_framework import viewsets, permissions
from serializers import BelongerSerializer

from webuser.models import Webuser

from rest_framework import permissions

from models import Belonger
from permissions import IsOwnerOrReadOnly

# Belonger is Meta, so 'with_name' version will appear in the end serializers

class BelongerViewSet(viewsets.ModelViewSet):
    pass
    #permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    
    def perform_create(self, serializer):
        uprofile = Webuser.objects.get(user=self.request.user)
        serializer.save(owner = uprofile)
    def get_queryset(self):
        qs = super(BelongerViewSet, self).get_queryset()
        if self.request.query_params.get('username'):
            qs = qs.filter(owner__user__username =
                    self.request.query_params.get('username'))
        return qs
