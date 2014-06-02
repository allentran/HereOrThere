from django.conf.urls import patterns, url

from FBLogin import views

urlpatterns = patterns('',
	url(r'^Test/$', views.test, name='FBindex'),
    url(r'^$', views.index, name='FBindex'),
    # ex: /login/
    url(r'^FB_success/$', views.FB_success, name='FBsuccess'),
    url(r'^FB_success/$', views.FB_success, name='FBsuccess'),
    url(r'^IG_success/$', views.IG_success, name='IGsuccess'),
)