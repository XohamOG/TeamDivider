from django.urls import path
from .views import PlayerListCreateAPIView, TeamFormationAPIView, SignupView, LoginView, LogoutView

urlpatterns = [
    path('players/', PlayerListCreateAPIView.as_view(), name='player-list-create'),
    path('teams/', TeamFormationAPIView.as_view(), name='team-formation'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
