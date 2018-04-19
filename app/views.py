#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 19, 2018, 8:07 AM
 * Software: PyCharm
 * Project Name: Tutorial
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime


def home(request):
    """
    Renders the home page.
    :param request:
    :return: title, year
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html', {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )

def contact(request):
    """
    Renders the contact page.
    :param request:
    :return: title, message, year
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html', {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )


def about(request):
    """
    Renders the about page.
    :param request:
    :return: titel, message, year
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html', {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )
