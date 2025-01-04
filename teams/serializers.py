from rest_framework import serializers
from .models import Player
from django.contrib.auth.models import User

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'position', 'rating', 'is_selected', 'user']  # Include 'user' if necessary
        read_only_fields = ['user']  # Prevent the user from being set via the API

class TeamSerializer(serializers.Serializer):
    team1 = serializers.ListField(child=serializers.CharField())
    team2 = serializers.ListField(child=serializers.CharField())

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user