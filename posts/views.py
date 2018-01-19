# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post

def post_create(request):
  form = PostForm(request.POST or None)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()

  context = {
    'form': form,
  }
  return render(request, "post_form.html", context)



def post_detail(request, id=None):
  instance = get_object_or_404(Post, id=id)

  context = {
    'title': "Detail",
    'instance': instance
  }
  return render(request, "post_detail.html", context)




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