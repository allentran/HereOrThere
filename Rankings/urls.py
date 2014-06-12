from django.conf.urls import patterns, include, url
import FBLogin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HereOrThere.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'Rankings.views.index', name='index'),
     url(r'^rankings', 'Rankings.views.public', name='Rankings:public'),
)
