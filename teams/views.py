from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Player
from .serializers import PlayerSerializer, TeamSerializer
from .utils import divide_into_teams

class PlayerListCreateAPIView(APIView):
    def get(self, request):
        """
        Retrieve the list of all players.
        """
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Add a new player to the database.
        """
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamFormationAPIView(APIView):
    def post(self, request):
        """
        Create teams based on selected players.
        """
        selected_player_ids = request.data.get('selected_players', [])
        if not selected_player_ids:
            return Response({'error': 'No players selected.'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the selected players
        selected_players = Player.objects.filter(id__in=selected_player_ids)

        if not selected_players.exists():
            return Response({'error': 'No valid players found.'}, status=status.HTTP_404_NOT_FOUND)

        # Divide players into teams
        team1, team2 = divide_into_teams(selected_players)
        return Response({'team1': [player.name for player in team1], 'team2': [player.name for player in team2]})
