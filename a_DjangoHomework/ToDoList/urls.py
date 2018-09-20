#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todolist/', views.index),
    path('todolist/add', views.submit_todolist, name='submit_todo'),
    path('todolist/get', views.get_todolist, name='get_todo')
]