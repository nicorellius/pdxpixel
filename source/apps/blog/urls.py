from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
    url(r'^logout/', 'blog.views.logout'),
)
