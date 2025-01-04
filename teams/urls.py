from django.urls import path
from .views import PlayerListCreateAPIView, TeamFormationAPIView, SignupView, LoginView, LogoutView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('players/', PlayerListCreateAPIView.as_view(), name='player-list-create'),
    path('teams/', TeamFormationAPIView.as_view(), name='team-formation'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),  # Custom JWT token obtain
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Standard JWT token refresh
]
