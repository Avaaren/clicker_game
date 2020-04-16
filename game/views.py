from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import TemplateView, View
from django.http import JsonResponse, HttpResponse
from django.db.models import F
from .models import Profile, GameSession


class GameView(TemplateView):

    template_name = 'game/game.html'


def ajax_result(request):

    if request.method == 'POST':

        user = request.user
        user_profile = get_object_or_404(Profile, user=user)
        score = request.POST.get('result')
        if score:
            # Create object of game
            GameSession.objects.create(
                user=user,
                score=score
            )# Problem in get_object_or_404!!!!
            # Update user info
            user_profile.games_played = F('games_played') + 1
            if int(score) > user_profile.high_score:
                user_profile.high_score = score
            user_profile.save()
            
        data = {
            'is_success': True,
            'url': reverse('result'),
        }
        return JsonResponse(data)






