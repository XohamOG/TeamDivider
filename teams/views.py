from django.shortcuts import render, redirect
from .models import Player
from .utils import divide_into_teams

def player_list(request):
    """
    Displays the list of players and allows users to select players for team division.
    """
    if request.method == 'POST':
        # Get selected player IDs from the form
        selected_player_ids = request.POST.getlist('selected_players[]')
        
        # Reset all players' is_selected to False
        Player.objects.update(is_selected=False)
        
        # Mark selected players as is_selected=True
        Player.objects.filter(id__in=selected_player_ids).update(is_selected=True)
        
        # Retrieve selected players for team division
        selected_players = Player.objects.filter(is_selected=True)
        
        # Generate teams using utility function
        team1, team2 = divide_into_teams(selected_players)
        
        # Render the team formation template with the generated teams
        return render(request, 'teams/team_formation.html', {'team1': team1, 'team2': team2})
    
    # If GET request, display all players
    players = Player.objects.all()
    return render(request, 'teams/player_list.html', {'players': players})


def add_player(request):
    """
    Allows users to add new players to the database.
    """
    if request.method == 'POST':
        # Extract data from the form
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        position = request.POST.get('position')
        
        # Validate data and create a new player
        if name and rating and position:
            Player.objects.create(
                name=name,
                rating=int(rating),
                position=position
            )
            return redirect('player_list')  # Redirect to the player list after adding
        
        # If invalid data, re-render the form with an error message
        return render(request, 'teams/add_player.html', {'error': 'All fields are required.'})
    
    # Render the add player form
    return render(request, 'teams/add_player.html')


def team_formation(request):
    """
    Displays the team formation results.
    """
    # This view is used in the player_list function after team generation.
    # It doesn't require direct handling here unless teams are saved for later use.
    pass
