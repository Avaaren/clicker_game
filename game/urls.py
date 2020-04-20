from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Game urls 
    path('', views.GameView.as_view(), name='game'),
    path('ajax_result/', views.ajax_result, name='ajax_result'),
    path('result/', views.ResultView.as_view(), name='result'),
    # Score urls
    path('leaderboard/', views.LeaderboardView.as_view(), name='leaderboard'),
    path('results/<str:user>/',
         views.UserResultsView.as_view(),
         name='user_results'),
    # Auth urls
    path('login/',
         auth_views.LoginView.as_view(
             template_name='auth/login.html'),
         name='login'),

    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='auth/password_reset.html',
             email_template_name='auth/password_reset_email.html'),
         name='password_reset'),

    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='auth/password_reset_done.html'),
         name='password_reset_done'),

    path('password_reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='auth/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='auth/password_reset_complete.html'),
         name='password_reset_complete'),
  
]
