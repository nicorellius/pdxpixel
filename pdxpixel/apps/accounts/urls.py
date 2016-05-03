from django.conf.urls import url
from django.contrib.auth.views import login, logout, logout_then_login

# from .views import UserLoginView


urlpatterns = [

    # url(r'^login/$', UserLoginView.as_view(), name='login'),

    url(r'^login/$', login, name='login'),

    # url(r'^logout/$', logout, name='logout'),

    url(r'^logout/$', logout_then_login, name='logout-then-login'),
]
