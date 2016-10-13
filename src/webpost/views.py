from models import Post
from rest_framework import viewsets, permissions
from serializers import PostSerializer
from permissions import IsOwnerOrReadOnly
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.contrib.auth import get_user_model


# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        qs = super(PostViewSet, self).get_queryset()
        if self.request.query_params.get('username'):
            qs = qs.filter(author__username=self.request.query_params.get('username'))
        return qs

    def perform_create(self, serializer):
        auth_type = ContentType.objects.get_for_model(get_user_model())
        serializer.save(author_id=self.request.user, author_type=auth_type)
