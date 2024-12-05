from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Player Name'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Player Rating'}),
        }
