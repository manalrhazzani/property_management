from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Phone number'})
    )

    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First name'})
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last name'})
    )

    role = forms.ChoiceField(  # 👈 Manually added role field
        choices=[
    ('CLIENT', 'Buyer'),
    ('AGENT', 'Real Estate Agent')
],
        widget=forms.Select(attrs={'id': 'id_role'}),
        required=True,
        label="Role"
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'phone', 'role', 'password1', 'password2'
        )
