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
from django.views.generic import TemplateView

import mothers.views

mothers_urls = [
    url(r'^$', TemplateView.as_view(template_name='mothers-list.html'), name='mother-list-template'),
    url(r'^apis$', mothers.views.MothersList.as_view(), name='mother-list'),
    url(r'^(?P<pk>\d+)$', TemplateView.as_view(template_name= 'mother-details.html'), name='mother-details-template'),
    url(r'^(?P<pk>\d+)/apis$', mothers.views.MotherDetails.as_view(), name='mother-details'),
    url(r'^new$', mothers.views.MotherDetails.as_view(), name='mother-new'),
    url(r'^pagination$', TemplateView.as_view(template_name='pagination.html')),
]

children_urls = [
    url(r'^$', TemplateView.as_view(template_name='children-list.html'), name='children-list-template'),
    url(r'^apis$', mothers.views.ChildrenList.as_view(), name='children-list'),
    url(r'^(?P<pk>\d+)/apis$', mothers.views.ChildDetails.as_view(), name='child-details'),
    url(r'^pagination$', TemplateView.as_view(template_name='pagination.html')),
]

donations_urls = [
    url(r'^$', TemplateView.as_view(template_name='donations-list.html'), name='donations-list-template'),
    url(r'^apis$', mothers.views.DonationsList.as_view(), name='donations-list'),
    url(r'^(?P<pk>\d+)/apis$', mothers.views.DonationDetails.as_view(), name='donation-details'),
    url(r'^pagination$', TemplateView.as_view(template_name='pagination.html')),
]

operators_urls = [
    url(r'^$', TemplateView.as_view(template_name='operators-list.html'), name='operators-list-template'),
    url(r'^apis$', mothers.views.OperatorsList.as_view(), name='operators-list'),
    url(r'^pagination$', TemplateView.as_view(template_name='pagination.html')),
]

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='mothers-list.html'), name='mother-list-template'),
    url(r'^mothers/', include(mothers_urls)),
    url(r'^children/', include(children_urls)),
    url(r'^donations/', include(donations_urls)),
    url(r'^operators/', include(operators_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += staticfiles_urlpatterns()

