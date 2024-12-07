from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.Serializer):
    team1 = serializers.ListField(child=serializers.CharField())
    team2 = serializers.ListField(child=serializers.CharField())
