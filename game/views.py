from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
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
            )  # Problem in get_object_or_404!!!!
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


class ResultView(TemplateView):

    template_name = 'game/result.html'

    def get_context_data(self, **kwargs):
        game_obj = GameSession.objects.filter(
            user=self.request.user
        ).order_by('-time')[:1][0]

        high_scores = GameSession.objects.all().order_by('-score')[:3]

        lower_results = GameSession.objects.filter(
            score__lte=game_obj.score
        ).exclude(
            pk=game_obj.pk
        ).order_by('-score', '-time')[:1]
        # Try except blocks add
        try: 
            higher_results = GameSession.objects.filter(
                score__gte=game_obj.score
            ).exclude(
                pk__in=[game_obj.pk, lower_results[0].pk]
            ).order_by('score', 'time')[:1]
        except IndexError:
            higher_results = GameSession.objects.filter(
                score__gte=game_obj.score
            ).exclude(
                pk__in=[game_obj.pk]
            ).order_by('score', 'time')[:1]
        
        for index, el in enumerate(GameSession.objects.order_by('-score', '-time')):
            if game_obj.pk == el.pk:
                your_place = index + 1

        data = super().get_context_data(**kwargs)

        if game_obj in high_scores:
            data['is_in_highscores'] = True

        data['game_result'] = game_obj
        data['high_scores'] = high_scores
        data['your_place'] = your_place
        data['lower_results'] = lower_results
        data['higher_results'] = higher_results
        return data


class UserResultsView(ListView):
    model = GameSession
    template_name = 'game/scores/user_results.html'
    context_object_name = 'results'

    def get(self, request, **kwargs):
        user = self.kwargs.get('user')

        if user == 'AnonymousUser':
            return redirect('login')
        
        return super(UserResultsView, self).get(request, **kwargs)

    def get_queryset(self, **kwargs):
        user = self.kwargs.get('user')

        user_results = GameSession.objects.filter(user__username=user).order_by('-time')
        return user_results


class LeaderboardView(ListView):
    model = GameSession
    template_name = 'game/scores/leaderboard.html'
    context_object_name = 'scores'
    paginate_by = 10

    def get_queryset(self):
        return GameSession.objects.order_by('-score', '-time')[:1000]
