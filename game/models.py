from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games_played = models.PositiveIntegerField(default=0)
    high_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class GameSession(models.Model):
    user = models.ForeignKey(User,
                             related_name='game_sessions',
                             on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(f'{self.pk} by {self.user}')
