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
