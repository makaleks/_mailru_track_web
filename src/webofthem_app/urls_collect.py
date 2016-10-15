# Router`s REST collection
from django.conf.urls import url, include
from rest_framework import routers

from webalbum.views import AlbumViewSet
from webchat.views import ChatViewSet
from webcomment.views import CommentViewSet
from weblike.views import LikeViewSet
from webmessage.views import MessageViewSet
from webphoto.views import PhotoViewSet
from webpost.views import PostViewSet
from webrelation.views import FriendshipViewSet
from webuser.views import UserViewSet, WebuserViewSet

router = routers.DefaultRouter()

router.register(r'albums', AlbumViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'friendships', FriendshipViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'webusers', WebuserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
