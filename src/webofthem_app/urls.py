"""webofthem_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.conf import settings

from .views import ApiAccess

from django.shortcuts import HttpResponseRedirect
def redirect_to_post_list(request):
    return HttpResponseRedirect('/posts/')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/hello', ApiAccess.as_view()),
    url(r'^api/', include('webofthem_app.urls_api_collect')),

    url(r'^login/', login, {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/', logout, {'template_name': 'core/logout.html'}, name="logout"),

    url(r'^$', redirect_to_post_list),
    url(r'^posts/', include('webpost.urls')),
    url(r'^chats/', include('webchat.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
