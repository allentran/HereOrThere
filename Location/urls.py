from django.conf.urls import patterns, url

from Location import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^instructions/', views.index, name='instructions'),
)
