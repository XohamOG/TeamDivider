from django.urls import path
from .views import PlayerListCreateAPIView, TeamFormationAPIView

urlpatterns = [
    path('players/', PlayerListCreateAPIView.as_view(), name='player-list-create'),
    path('teams/', TeamFormationAPIView.as_view(), name='team-formation'),
]
