from django import urls

from . import views

urlpatterns = [
    path('', views.GameView.as_view(), name='game'),
]