from django.db import models
from clients.models import Client
from biens.models import Bien
from django.utils import timezone

from django.db import models
from clients.models import Client
from biens.models import Bien

class RendezVous(models.Model):
    date = models.DateField()
    time = models.TimeField()  # anciennement heure
    property = models.ForeignKey(Bien, on_delete=models.CASCADE)  # anciennement bien
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)  # anciennement commentaire
    status = models.CharField(max_length=20, choices=[
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ], default='Scheduled')  # anciennement statut

    def __str__(self):
        return f"{self.client} - {self.property} - {self.date} {self.time}"