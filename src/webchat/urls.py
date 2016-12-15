from django.conf.urls import url, include
from views import render_chat_list, render_chat

urlpatterns = [
    url(r'^$', render_chat_list),
    url(r'^(?P<pk>\d+)/$', render_chat)
]
