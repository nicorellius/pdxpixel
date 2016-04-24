from django.conf.urls import include, url
from django.contrib import admin

# error pages
handler400 = 'core.views.custom_bad_request'
handler403 = 'core.views.custom_permission_denied'
handler404 = 'core.views.custom_page_not_found'
handler500 = 'core.views.custom_server_error'
handler502 = 'core.views.custom_bad_gateway'

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),

    # url(r'^(\d)/$', 'core.views.custom_server_error'),
]
