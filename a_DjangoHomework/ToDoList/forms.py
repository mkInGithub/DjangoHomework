#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms

from .models import ToDoList


class ToDoListForm(forms.ModelForm):
    # label="" 页面上就只看到输入框
    content = forms.CharField(label='')

    class Meta:
        model = ToDoList
        fields = ('content',)
