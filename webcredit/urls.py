"""webcredit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from collection import views
from collection.backends import MyRegistrationView

from django.contrib.auth.views import(
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
    password_change
    )

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^about/$',
		TemplateView.as_view(template_name='about.html'),
		name = 'about'),
	url(r'^contact/$',
		TemplateView.as_view(template_name='contact.html'),
		name = 'contact'),
    url(r'^list/$', views.list, name='list'),
    url(r'^accounts/',
        include('registration.backends.simple.urls')),
#the new password reset URLs
    url(r'^accounts/password/reset/$',
        password_reset,
        {'template_name':
        'registration/password_reset_form.html'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name':
        'registration/password_reset_done.html'},
        name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {'template_name':
        'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$',
        password_reset_complete,
        {'template_name':
        'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    url(r'^accounts/password/change/form/$',
        password_change,
        {'template_name':
        'registration/password_change_form.html'},
        name="password_change_form"),
    url(r'^accounts/register/$',
        MyRegistrationView.as_view(),
        name='registration_register'),

    url(r'^accounts/',
        include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),


]