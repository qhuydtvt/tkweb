__author__ = 'qhuydtvt'

from . import views
from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'techkids.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name="index"),
	url(r'^about/', views.about, name="about"),
	url(r'^contact/', views.contact, name="contact"),
	url(r'^courses/', views.courses, name="courses"),
    url(r'^student-portfolio/', views.portfolio, name="portfolio"),
	url(r'^course/([0-9]+)/$', views.course_single, name="course_single"),
    url(r'^instructor/([0-9]+)/$', views.instructor_single, name="instructor_single"),
]
