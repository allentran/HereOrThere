from django.conf.urls import patterns, include, url
import FBLogin
from django.contrib import admin
import Rankings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'HereOrThere.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('SiteUsers.urls',namespace='SiteUsers')),
    url(r'^locate/', include('Location.urls',namespace='Location')),
    url(r'^sheepoff/', include('Battles.urls',namespace='Battles')),
    url(r'^instagram/', include('Instagram.urls',namespace='Instagram')),
    url(r'^errors/', include('Errors.urls',namespace='Errors')),
    url(r'^rankings/', include('Rankings.urls',namespace='Rankings')),
)
