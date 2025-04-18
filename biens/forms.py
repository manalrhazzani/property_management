from django import forms
from .models import Bien

class BienForm(forms.ModelForm):
    class Meta:
        model = Bien
        fields = '__all__'
        labels = {
            'image': '📷 Photo',
        }
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control custom-input',
                'placeholder': 'Ajoutez une description...'
            }),
            # Pas de widget pour image => laisse ClearableFileInput par défaut
        }
