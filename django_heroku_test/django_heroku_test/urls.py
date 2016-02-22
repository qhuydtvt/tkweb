from django.conf.urls import include, url
from django.contrib import admin
import cms

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_heroku_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cms/', include('cms.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
