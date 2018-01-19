# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

def post_create(request):
  return HttpResponse("<h1>Hello CREATE</h1>")

def post_detail(request):
  return HttpResponse("<h1>Hello DETAIL</h1>")

def post_list(request):
  return HttpResponse("<h1>Hello LIST</h1>")

def post_update(request):
  return HttpResponse("<h1>Hello UPDATE</h1>")

def post_delete(request):
  return HttpResponse("<h1>Hello DELETE</h1>")