from django.conf.urls import patterns, include, url
import FBLogin
from django.contrib import admin
import Rankings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HereOrThere.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'Rankings.views.public', name='public'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('SiteUsers.urls',namespace='SiteUsers')),
    url(r'^locate/', include('Location.urls',namespace='Location')),
    url(r'^battle/', include('Battles.urls',namespace='Battles')),
    url(r'^instagram/', include('Instagram.urls',namespace='Instagram')),
)
