# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .models import Post

def post_create(request):
  context = {
    'title': "Create"
  }
  return render(request, "index.html", context)

def post_detail(request):
  context = {
    'title': "Detail"
  }
  return render(request, "index.html", context)

def post_list(request):
  queryset = Post.objects.all()
  # if request.user.is_authenticated():
  #   context = {
  #   'title': "Admin List"
  #   }
  # else:
  #   context = {
  #     'title': "List"
  #   }
  context = {
      'title': "List",
      'queryset': queryset
    }
  
  return render(request, "index.html", context)

def post_update(request):
  context = {
    'title': "Update"
  }
  return render(request, "index.html", context)

def post_delete(request):
  context = {
    'title': "Delete"
  }
  return render(request, "index.html", context)