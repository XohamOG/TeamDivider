from django.shortcuts import redirect, render
from .models import Player
from teams.forms import PlayerForm
from teams.utils import divide_players_into_teams

def team_balancer(request):
    if request.method == 'POST':
        if 'clear' in request.POST:
            Player.objects.all().delete()
            return redirect('team_balancer')

        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_balancer')
    else:
        form = PlayerForm()

    players = Player.objects.all()
    team1, team2 = divide_players_into_teams(players)

    return render(request, 'teams/team_balancer.html', {
        'form': form,
        'team1': team1,
        'team2': team2
    })
