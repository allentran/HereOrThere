from django.conf.urls import patterns, url

from Battles import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
