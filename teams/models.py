from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    position = models.CharField(max_length=50, choices=[('Goalkeeper', 'Goalkeeper'), ('Player', 'Player')], default='Player')
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return self.name
