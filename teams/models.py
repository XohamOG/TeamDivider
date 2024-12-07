from django.db import models

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

    def __str__(self):
        return self.name

