from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games_played = models.PositiveIntegerField(default=0)
    high_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username


class GameSession(models.Model):
    user = models.ForeignKey(User,
                             related_name='game_sessions',
                             on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(f'{self.pk} by {self.user}')
