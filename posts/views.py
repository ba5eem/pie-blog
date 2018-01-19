# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView

from .forms import PostForm
from .models import Post

# POST CREATE ********************

def post_create(request):
  form = PostForm(request.POST or None, request.FILES or None)
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


# class PostDetailView(DetailView):
#   template_name = 'post_detail.html' 
  
#   def get_object(self, *args, **kwargs):
#     slug = self.kwargs.get("slug")
#     instance = get_object_or_404(Post, slug=slug)
#     if instance.publish > timezone.now().date() or instance.draft:
#       if not request.user.is_staff or not request.user.is_superuser:
#         raise Http404
#     return instance
  
#   def get_context_data(self, *args, **kwargs):
#     context = super(PostDetailView, self).get_context_data(*args, **kwargs)
#     instance = context['object']
#     context['share_string'] = quote_plus(instance.content)
#     return context

def post_detail(request, id=None):
  instance = get_object_or_404(Post, id=id)

  context = {
    'title': instance.title,
    'instance': instance,
  }
  return render(request, "post_detail.html", context)


# POST LIST ********************


def post_list(request):
  queryset_list = Post.objects.all()
  paginator = Paginator(queryset_list, 5) # Show 25 posts per page
  page = request.GET.get('page')
  try:
    queryset = paginator.page(page)
  except PageNotAnInteger:
    queryset = paginator.page(1)
  except EmptyPage:
    queryset = paginator.page(paginator.num_pages)

  context = {
      'title': "List",
      'queryset': queryset
    }
  
  return render(request, "post_list.html", context)





# POST UPDATE ********************

def post_update(request, id=None):
  instance = get_object_or_404(Post, id=id, )
  form = PostForm(request.POST or None,request.FILES or None,  instance=instance)
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
