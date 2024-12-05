from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_balancer, name='team_balancer'),
]
