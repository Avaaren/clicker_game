from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games_played = models.PositiveIntegerField(default=0)
    high_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.name




