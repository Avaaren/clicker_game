from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

app_name = 'account'

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(
             template_name='account/login.html'),
         name='login'),

    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signup-done/', views.SignupDoneView.as_view(), name='signup-done'),

    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='account/password_reset.html',
             email_template_name='account/password_reset_email.html',
             success_url=reverse_lazy('account:password_reset_done'),),
         name='password_reset'),

    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/password_reset_done.html'),
         name='password_reset_done'),

    path('password_reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password_reset_confirm.html',
             success_url=reverse_lazy('account:password_reset_complete'),),
         name='password_reset_confirm'),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),

]
