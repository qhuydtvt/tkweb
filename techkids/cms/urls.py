__author__ = 'qhuydtvt'

from . import views
from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'techkids.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	
    url(r'^$', views.index, name="index"),
	url(r'^about/', views.about, name="about"),
	url(r'^courses/', views.courses, name="courses"),
	url(r'^course/1337/', views.courseSingle, name="courseSingle"),
]
