from .import views
from django.conf.urls import url, include

from django.contrib.auth import views as auth_views


urlpatterns = [

    url(r'^login/$', views.user_login, name="login"),
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^statements/$', views.billing, name="billing"),
    url(r'^profile/$', views.profile, name="profile"),
    #url(r'^login$', views.user_login, name="login"),
    #url(r'^login/$', auth_views.LoginView, name='login'),

]
