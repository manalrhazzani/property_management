from django.contrib import admin
from .models import Client, Interaction

class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'phone', 'client_type', 'property')  # Champs modifiés
    search_fields = ('last_name', 'first_name', 'email', 'phone', 'client_type')  # Champs modifiés
    list_filter = ('client_type', 'property')  # Filtrage par client_type et property

class InteractionAdmin(admin.ModelAdmin):
    list_display = ('client', 'interaction_type', 'date', 'comment')  # Champs modifiés
    search_fields = ('client__last_name', 'client__first_name', 'interaction_type', 'comment')
    list_filter = ('interaction_type', 'date')

admin.site.register(Client, ClientAdmin)
admin.site.register(Interaction, InteractionAdmin)
