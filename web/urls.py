"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

import mothers.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mothers.views.ListMothersView.as_view(), name='mothers-list',),
    url(r'^children$', mothers.views.ListChildrenView.as_view(), name='children-list',),
    url(r'^donations$', mothers.views.ListDonationsView.as_view(), name='donations-list',),
    url(r'^mothers/new$', mothers.views.CreateMotherView.as_view(), name='mother-new',),
    url(r'^mothers/edit/(?P<pk>\d+)/$', mothers.views.UpdateMotherView.as_view(), name='mother-edit',),
    url(r'^mothers/view/(?P<pk>\d+)/$', mothers.views.MotherDetailView.as_view(), name='mother-view',),
]

urlpatterns += staticfiles_urlpatterns()

