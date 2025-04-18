# clients/apps.py

from django.apps import AppConfig

class ClientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clients'

    def ready(self):
        import clients.signals  # 👈 c'est ce qui déclenche les signaux
