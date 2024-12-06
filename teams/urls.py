from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_list, name='player_list'),
    path('add/', views.add_player, name='add_player'),
    path('teams/', views.team_formation, name='team_formation'),
]
