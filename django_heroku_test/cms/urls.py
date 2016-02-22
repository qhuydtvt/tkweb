from django.conf.urls import url

__author__ = 'qhuydtvt'

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]