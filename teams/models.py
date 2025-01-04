from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    POSITION_CHOICES = [
        ('Goalkeeper', 'Goalkeeper'),
        ('Attacker', 'Attacker'),
        ('Defender', 'Defender'),
        ('Player', 'Player'),
    ]
    
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, default='Player')
    is_selected = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="players")

    def __str__(self):
        return f"{self.name} ({self.user.username})"

