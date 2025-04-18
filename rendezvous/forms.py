from django import forms
from .models import RendezVous

class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ['property', 'client', 'date', 'time', 'comment', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
# formulaire pour le client
class PrendreRendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ['property', 'date', 'time', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }