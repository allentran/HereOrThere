from django.conf.urls import patterns, include, url
import FBLogin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HereOrThere.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('SiteUsers.urls')),
    url(r'^locate/', include('Location.urls')),
    url(r'^battle/', include('Battles.urls')),
)
