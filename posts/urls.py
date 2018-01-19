from django.conf.urls import url
from django.contrib import admin
from posts import views as post_view

urlpatterns = [
    url(r'^$', post_view.post_list, name='list'),
    url(r'^create/$', post_view.post_create),
    url(r'^(?P<id>[\w-]+)/$', post_view.post_detail, name='detail'),
    url(r'^(?P<id>[\w-]+)/edit$', post_view.post_update, name="update"),
    url(r'^(?P<id>[\w-]+)/delete/$', post_view.post_delete, name='delete')
]
