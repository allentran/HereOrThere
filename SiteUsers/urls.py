from django.conf.urls import patterns, url

from SiteUsers import views

urlpatterns = patterns('',
	url(r'^register/$', views.register, name='registernew'),
)