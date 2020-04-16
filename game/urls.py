from django.urls import path

from . import views

urlpatterns = [
    path('', views.GameView.as_view(), name='game'),
    path('ajax_result/', views.ajax_result, name='ajax_result'),
    path('result/', views.ResultView.as_view(), name='result'),
]