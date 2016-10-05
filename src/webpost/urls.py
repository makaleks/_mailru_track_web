from django.conf.urls import url, include
from webposts.models import Post
from rest_framework import routers, serializers, viewsets

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('text', 'author')

# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Routers provide an easy way of automatically determining the URL conf.
router.register(r'users', PostViewSet)

