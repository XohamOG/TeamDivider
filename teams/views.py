from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Player
from .serializers import PlayerSerializer, TeamSerializer, UserSerializer
from .utils import divide_into_teams

# views.py
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class PlayerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


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

class SignupView(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')

            if not username or not password:
                return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

            # Check if user already exists
            if User.objects.filter(username=username).exists():
                return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(username=username, password=password)
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):

    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)