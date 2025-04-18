from django.contrib import admin
from .models import RendezVous

class RendezVousAdmin(admin.ModelAdmin):
    list_display = ('client', 'property', 'date', 'time', 'status', 'comment')
    search_fields = ('client__last_name', 'client__first_name', 'property__title', 'status')
    list_filter = ('status', 'date')
    ordering = ('-date', '-time')
    date_hierarchy = 'date'

admin.site.register(RendezVous, RendezVousAdmin)
