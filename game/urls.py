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
]
