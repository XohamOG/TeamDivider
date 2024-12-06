import random

def divide_into_teams(players):
    players = list(players)
    random.shuffle(players)

    # Separate goalkeepers
    goalkeepers = [player for player in players if player.position == 'Goalkeeper']
    field_players = [player for player in players if player.position != 'Goalkeeper']

    # Randomly assign one goalkeeper to each team
    team1 = [goalkeepers.pop()] if goalkeepers else []
    team2 = [goalkeepers.pop()] if goalkeepers else []

    # Split field players
    midpoint = len(field_players) // 2
    team1.extend(field_players[:midpoint])
    team2.extend(field_players[midpoint:])

    return team1, team2
