from django.conf.urls import url
from django.contrib import admin
from posts import views as post_view

urlpatterns = [
    url(r'^$', post_view.post_list),
    url(r'^create/$', post_view.post_create),
    url(r'^(?P<id>\d+)/$', post_view.post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit$', post_view.post_update, name="update"),
    url(r'^delete/$', post_view.post_delete)
]
