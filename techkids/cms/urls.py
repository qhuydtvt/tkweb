__author__ = 'qhuydtvt'

from . import views
from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'techkids.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^node/', views.node, name="node"),
    url(r'^$', views.index, name="index"),
]
