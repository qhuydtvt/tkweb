from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'techkids.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cms/', include('cms.urls'), name="cms"),
    url(r'^admin/', include(admin.site.urls), name="home"),
]
