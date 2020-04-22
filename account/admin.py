from django.contrib import admin

from game.models import (
    Profile,
)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    class Meta:
        list_display = ('pk', 'user', 'games_played', 'high_score')
