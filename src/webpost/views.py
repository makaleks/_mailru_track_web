from models import Post
from rest_framework import viewsets, permissions
from serializers import PostSerializer
from permissions import IsOwnerOrReadOnly
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.contrib.auth import get_user_model
from webinteractive.views import BelongerViewSet

from django.shortcuts import render
from django.http import HttpResponse

# ViewSets define the view behavior.
class PostViewSet(BelongerViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def render_post_list(request):
    return render(request, 'post_list.html', {
            'post_list': Post.objects.all(),
        })
