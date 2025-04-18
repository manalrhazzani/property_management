from django import forms
from .models import Client,Bien
from .models import Interaction

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['last_name', 'first_name', 'email', 'phone', 'client_type', 'property']  # Champs modifiés

    property = forms.ModelChoiceField(queryset=Bien.objects.all(), required=False)  # bien -> property

class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ['interaction_type', 'comment']  # type_interaction -> interaction_type, commentaire -> comment
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
