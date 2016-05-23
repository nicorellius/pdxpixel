from django.conf.urls import url

from .views import PostListView, GetPostDetailView
from .views import TagListView, TagIndexView

urlpatterns = [

    url(r'^$', PostListView.as_view(), name='post-list'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<entry>[-\w]+)/$',
        GetPostDetailView.as_view(),
        name='post-detail'),

    url(r'^tags/', TagListView.as_view(), name='tag-list'),

    url(r'^tag/(?P<slug>[-\w]+)/$', TagIndexView.as_view(), name='tagged'),
]
