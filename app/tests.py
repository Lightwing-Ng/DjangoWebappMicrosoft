#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 19, 2018, 8:07 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import django
from django.test import TestCase


# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """
    Tests for the application views.
    """

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """
        Tests the home page.
        :return: 200
        """
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 1, 200)

    def test_contact(self):
        """
        Tests the contact page.
        :return: 200
        """
        response = self.client.get('/contact')
        self.assertContains(response, 'Contact', 3, 200)

    def test_about(self):
        """
        Tests the about page.
        :return: 200
        """
        response = self.client.get('/about')
        self.assertContains(response, 'About', 3, 200)
