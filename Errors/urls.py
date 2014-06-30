from django.conf.urls import patterns, url

from Errors import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    )
