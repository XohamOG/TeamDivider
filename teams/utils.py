import random

def divide_players_into_teams(players):
    """
    Divides players into two balanced teams with equal sizes and assigns a goalkeeper to each team.
    :param players: List of player objects with 'rating' attributes
    :return: Two dictionaries representing the teams with players and goalkeepers
    """
    if len(players) < 2:
        return {"goalkeeper": None, "players": players}, {"goalkeeper": None, "players": []}
    
    # Sort players by rating (descending)
    players = sorted(players, key=lambda x: x.rating, reverse=True)

    # Assign goalkeepers randomly
    goalkeepers = random.sample(players, 2)
    players = [player for player in players if player not in goalkeepers]

    # Initialize teams
    team1 = {"goalkeeper": goalkeepers[0], "players": []}
    team2 = {"goalkeeper": goalkeepers[1], "players": []}

    # Distribute remaining players into teams
    for player in players:
        if len(team1["players"]) <= len(team2["players"]):
            team1["players"].append(player)
        else:
            team2["players"].append(player)

    return team1, team2
