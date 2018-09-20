#!/usr/bin/env python
# -*- coding: utf-8 -*-
import django.core.handlers.base
import re
from django.shortcuts import render


# 判断用户IE版本的中间件
class CheckBrowserMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        browser = request.META["HTTP_USER_AGENT"]
        # print(browser)
        # print(request.META)
        # browser_dict = {
        #     'IE9': "MSIE 9.0",
        #     'IE8': "MSIE 8.0",
        #     'IE7': "MSIE 7.0",
        #     'IE6': "MSIE 6.0",
        #     'MAXTHON': "Maxthon",
        #     'QQ': "QQBrowser",
        #     'GREEN': "GreenBrowser",
        #     'SE360': "360SE",
        #     'FIREFOX': "Firefox",
        #     'OPERA': "Opera",
        #     'CHROME': "Chrome",
        #     'SAFARI': "Safari",
        #     'OTHER': "其它",
        # }
        browser_cannot_used = ["MSIE 8.0", "MSIE 7.0", "MSIE 6.0"]
        for b in browser_cannot_used:
            if re.search(b, browser):
                return render(request, 'IE2Low.html')

        response = self.get_response(request)
        return response
