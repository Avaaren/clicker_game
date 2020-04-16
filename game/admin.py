from django.contrib import admin

from .models import (
    GameSession,
    Profile
)


@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'score', 'time')


@admin.register(Profile)
class ProfileSessionAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = ('pk', 'user', 'games_played', 'high_score')