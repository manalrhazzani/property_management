from django.db.models.signals import post_save
from django.dispatch import receiver
from clients.models import Client, Bien
from utilisateurs.models import User  # adapte si besoin

@receiver(post_save, sender=User)
def create_client_profile(sender, instance, created, **kwargs):
    if created and instance.role == User.Role.CLIENT:
        print(f"✔ Création automatique du profil client pour {instance.username}")
        
        # Récupération des données
        phone = getattr(instance, 'phone', '') or ''
        client_type = 'Buyer'  # ou 'Tenant', selon ta logique métier
        property_obj = None  # Tu peux associer un bien plus tard si besoin

        # Création du profil client avec les bons noms de champs
        Client.objects.create(
            user=instance,
            last_name=instance.last_name or '',
            first_name=instance.first_name or '',
            email=instance.email,
            phone=phone,
            client_type=client_type,
            property=property_obj
        )
