from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class User(AbstractUser):
    """Modèle utilisateur personnalisé avec système de rôles"""
    
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', _('Admin')
        AGENT = 'AGENT', _('Agent')
        CLIENT = 'CLIENT', _('Client')
    
    # Validateur pour le numéro de téléphone
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("Format : '+999999999'. Jusqu'à 15 chiffres.")
    )
    
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CLIENT,
        verbose_name=_('Role'),
        help_text=_('Role determining permissions')
    )
    
    phone = models.CharField(  # Changement ici
        db_column='phone',
        max_length=20,
        validators=[phone_regex],
        blank=True,
        null=True,
        verbose_name=_('phone'),
        help_text=_('main contact number')
    )
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['last_name', 'first_name']
        permissions = [
            ("can_promote_agent", " can promote a client to an agent"),
        ]

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_role_display()})"
    
    def save(self, *args, **kwargs):
        """S'assure que les superutilisateurs ont le rôle ADMIN"""
        if self.is_superuser:
            self.role = self.Role.ADMIN
        super().save(*args, **kwargs)
    
    # Méthodes de rôle
    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN
    
    @property
    def is_agent(self):
        return self.role == self.Role.AGENT
    
    @property
    def is_client(self):
        return self.role == self.Role.CLIENT


from django.contrib.auth import get_user_model

User = get_user_model()

class DemandeAgent(models.Model):
    STATUT_CHOICES = [
    ('Pending', _('Pending')),
    ('Accepted', _('Accepted')),
    ('Rejected', _('Rejected')),
]


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    date_demande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.statut}" 