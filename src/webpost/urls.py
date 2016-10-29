from django.conf.urls import url, include
from views import render_post_list, render_post

urlpatterns = [
    url(r'^$', render_post_list),
    url(r'^(?P<pk>\d+)/$', render_post)
    # Django reverse
    # model::get_absolute_url
]
