# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

# POST CREATE ********************

def post_create(request):
  form = PostForm(request.POST or None)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    messages.success(request, "Successfully Created", extra_tags='html_safe')
    return HttpResponseRedirect(instance.get_absolute_url())

  context = {
    'form': form,
    'submit': "Create Post"
  }
  return render(request, "post_form.html", context)

# POST DETAIL ********************

def post_detail(request, id=None):
  instance = get_object_or_404(Post, id=id)

  context = {
    'title': instance.title,
    'instance': instance
  }
  return render(request, "post_detail.html", context)


# POST LIST ********************


def post_list(request):
  queryset = Post.objects.all()
  context = {
      'title': "List",
      'queryset': queryset
    }
  
  return render(request, "post_list.html", context)



# POST UPDATE ********************

def post_update(request, id=None):
  instance = get_object_or_404(Post, id=id)
  form = PostForm(request.POST or None, instance=instance)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    messages.success(request, "Successfully Saved")
    return HttpResponseRedirect(instance.get_absolute_url())

  context = {
    'title': instance.title,
    'instance': instance,
    "form": form,
    "submit": "Submit Edit"
  }
  return render(request, "post_form.html", context)


# POST DELETE ********************


def post_delete(request, id=None):
  instance = get_object_or_404(Post, id=id)
  instance.delete()
  messages.success(request, "Successfully Deleted")
  return redirect('posts:list')
