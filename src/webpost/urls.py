from django.conf.urls import url, include
from views import render_post_list

urlpatterns = [
    url(r'^$', render_post_list)
]
