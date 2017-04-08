from django.conf.urls import include, url
from django.shortcuts import get_object_or_404, render
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'veena.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('mani.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]
