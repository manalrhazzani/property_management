from django.db import models
from biens.models import Bien
from django.conf import settings

from utilisateurs.models import User

 

class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    last_name = models.CharField(max_length=100)  # Nom -> last_name
    first_name = models.CharField(max_length=100)  # Prénom -> first_name
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    CLIENT_TYPE_CHOICES = [
        ('Buyer', 'Buyer'),  # Acheteur -> Buyer
        ('Tenant', 'Tenant'),  # Locataire -> Tenant
    ]
    client_type = models.CharField(max_length=10, choices=CLIENT_TYPE_CHOICES, default='Buyer')  # type_client -> client_type
    property = models.ForeignKey('biens.Bien', on_delete=models.SET_NULL, null=True, blank=True, related_name="interested_clients")  # bien -> property, on spécifie 'biens.Bien'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from .models import Client   

class Interaction(models.Model):
    INTERACTION_TYPE_CHOICES = [
        ('Call', 'Call'),  # Appel -> Call
        ('Visit', 'Visit'),  # Visite -> Visit
        ('Meeting', 'Meeting'),  # Rendez-vous -> Meeting
        ('Note', 'Note'),  # Note -> Note
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=20, choices=INTERACTION_TYPE_CHOICES)  # type_interaction -> interaction_type
    comment = models.TextField()  # commentaire -> comment
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.interaction_type} - {self.client.first_name} {self.client.last_name} - {self.date.strftime('%d/%m/%Y')}"
