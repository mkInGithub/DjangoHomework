#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytz
from django import template

register = template.Library()
from django.template import defaultfilters


def since_now1(value, format):
    import datetime
    oldtime = datetime.datetime.strptime(value, format)
    nowtime = datetime.datetime.now()
    otm = oldtime.month
    oty = oldtime.year
    from datetime import timedelta
    if oldtime > nowtime:
        return "当前时间小于建立时间"
    try:
        res = nowtime - oldtime
    except:
        return None
    if oldtime.replace(year=(oty + 1)) < nowtime:
        return "发布于1年前"
    elif oldtime.replace(month=(otm + 1)) < nowtime:
        return "发布于1月前"
    elif res.days >= 7:
        return "发布于1周前"
    elif 7 > res.days >= 1:
        return "发布于1天前"
    elif res.seconds > 3600:
        return "发布于%d小时前" % (res.seconds / 3600)
    elif res.seconds > 60:
        return "发布于%d分钟前" % (res.seconds / 60)
    else:
        return "发布于%d秒前" % (res.seconds)
register.filter('since_now1', since_now1)

def since_now2(value):
    import datetime
    oldtime = value.replace(tzinfo=None)
    oldtime = oldtime + datetime.timedelta(seconds=3600*8)
    nowtime = datetime.datetime.now()
    otm = oldtime.month
    oty = oldtime.year
    if oldtime > nowtime:
        return "当前时间小于建立时间"
    try:
        res = nowtime - oldtime
    except:
        return None
    if oldtime.replace(year=(oty + 1)) < nowtime:
        return "发布于1年前"
    elif oldtime.replace(month=(otm + 1)) < nowtime:
        return "发布于1月前"
    elif res.days >= 7:
        return "发布于1周前"
    elif 7 > res.days >= 1:
        return "发布于1天前"
    elif res.seconds > 3600:
        return "发布于%d小时前" % (res.seconds / 3600)
    elif res.seconds > 60:
        return "发布于%d分钟前" % (res.seconds / 60)
    else:
        return "发布于%d秒前" % (res.seconds)
register.filter('since_now2', since_now2)
