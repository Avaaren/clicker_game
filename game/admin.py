from django.contrib import admin

from .models import (
    GameSession,
)


@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'score', 'time')


