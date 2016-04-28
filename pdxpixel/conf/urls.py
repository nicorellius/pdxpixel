from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.flatpages import views

from django.views.generic import TemplateView

# error pages
handler400 = 'core.views.custom_bad_request'
handler403 = 'core.views.custom_permission_denied'
handler404 = 'core.views.custom_page_not_found'
handler500 = 'core.views.custom_server_error'
handler502 = 'core.views.custom_bad_gateway'

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name="base.html"), name='home-page-view'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^blog/', include('apps.blog.urls', namespace='blog', app_name='blog')),

    # url(r'^(\d)/$', 'core.views.custom_server_error'),
]

# catchall for flatpages
urlpatterns += [url(r'^(?P<url>.*)$', views.flatpage)]

urlpatterns += staticfiles_urlpatterns()
