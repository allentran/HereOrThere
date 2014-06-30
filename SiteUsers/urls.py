from django.conf.urls import patterns, url

from SiteUsers import views

urlpatterns = patterns('',
	url(r'^register/$', views.register, name='register'),
	url(r'^logout/$',views.logout_view, name='logout'),
	url(r'^login/$',views.login_view, name='login'),
	url(r'^instagram/$',views.instagram, name='instagram'),
)