from django.conf.urls import url, include
from webmessage.models import Message
from rest_framework import routers, serializers, viewsets

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('author', 'text')

# ViewSets define the view behavior.
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# Routers provide an easy way of automatically determining the URL conf.
router.register(r'users', MessageViewSet)

