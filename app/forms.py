#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 19, 2018, 8:06 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    """
    Authentication form which uses boostrap CSS.
    """
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            {
                'class': 'form-control',
                'placeholder': 'User name'
            }
        )
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            {'class': 'form-control',
             'placeholder': 'Password'}
        )
    )
