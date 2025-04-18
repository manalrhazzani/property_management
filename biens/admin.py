from django.contrib import admin
from .models import Bien, Photo



class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
class BienAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'status', 'price', 'area', 'city', 'bedroom', 'added_on')  # Added 'bedroom'
    search_fields = ('title', 'address', 'type', 'status', 'city', 'bedroom')  # Added 'bedroom'
    list_filter = ('type', 'status', 'city', 'bedroom')  # Added 'bedroom' to filter options
    ordering = ('-added_on',)
    date_hierarchy = 'added_on'
    inlines= [PhotoInline]

admin.site.register(Bien, BienAdmin)
admin.site.register(Photo)
