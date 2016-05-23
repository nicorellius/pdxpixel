from django.conf.urls import url
from django.contrib.auth.views import logout, logout_then_login

from .views import LoginView, LogoutView, ProfileView


urlpatterns = [

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout-then-login'),

    url(r'^profile/$', ProfileView.as_view(), name='profile'),
]
