from models import Post
from rest_framework import viewsets, permissions
from serializers import PostSerializer
from permissions import IsOwnerOrReadOnly


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
        serializer.save(author_id=self.request.user)
