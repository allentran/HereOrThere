from django.conf.urls import patterns, include, url
import FBLogin
from django.contrib import admin
from Instagram import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HereOrThere.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^$', 'Instagram.views.redirect', name='redirect'),
)
