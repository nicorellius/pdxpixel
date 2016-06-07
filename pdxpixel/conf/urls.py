from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.flatpages import views
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from apps.blog.sitemaps import PostSitemap


# error pages
handler400 = 'core.views.custom_bad_request'
handler403 = 'core.views.custom_permission_denied'
handler404 = 'core.views.custom_page_not_found'
handler500 = 'core.views.custom_server_error'
handler502 = 'core.views.custom_bad_gateway'

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name="index.html"),
        name='home-page-view'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('apps.accounts.urls',
                               namespace='accounts',
                               app_name='accounts')),

    url(r'^blog/', include('apps.blog.urls', namespace='blog', app_name='blog')),

    url(r'^sitemap\.xml$', sitemap, {
        'sitemaps': sitemaps
    }, name='django.contrib.sitemaps.views.sitemap'),

    url(r"^search/", include("watson.urls", namespace="watson"), {
        'template_name': 'search/default.html',
        'context_object_name': 'results',
    }),

    url(r'^contact/$', views.flatpage, {'url': '/contact/'}, name='contact'),
    url(r'^nick-vincent-maloney/$', views.flatpage, {
        'url': '/nick-vincent-maloney/'
    }, name='nicks-resume'),

    # url(r'^(\d)/$', 'core.views.custom_server_error'),
]

# catchall for flatpages
# urlpatterns += [url(r'^(?P<url>.*)/$', views.flatpage)]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)