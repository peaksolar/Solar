from .import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views


urlpatterns = [

    url(r'^login/$', views.user_login, name="login"),
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^statements/$', views.billing, name="billing"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^comments/$', views.comments, name="comments"),
    url(r'^forgotpassword/$', views.forgotpassword, name="forgotpassword"),
    url(r'^register/$', views.register, name="register"),
    url(r'^edit/$', views.edit, name="edit"),
    url(r'^password-change/$', views.change_password, name="password_change"),
    url(r'^password-change/done/$', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    url(r'^password-reset/$', auth_views.PasswordResetView.as_view(), name="password_reset"),
    url(r'^password-reset/done/$', auth_views.PasswordChangeDoneView.as_view(), name="password_reset_done"),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.PasswordResetConfirmView, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    # url(r'^login$', views.user_login, name="login"),
    # url(r'^login/$', auth_views.LoginView, name='login'),

]