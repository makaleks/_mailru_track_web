from webinteractive.views import InteractiveViewSet

from serializers import CommentSerializer
from models import Comment


class CommentViewSet(InteractiveViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
