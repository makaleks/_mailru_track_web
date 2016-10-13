# Router`s REST collection
from django.conf.urls import url, include
from rest_framework import routers
from webuser.views import UserViewSet
from webpost.views import PostViewSet
from webrelation.views import FriendshipViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'friendships', FriendshipViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
