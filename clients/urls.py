from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),  # Accueil
    path('clients/', views.client_list, name='client_list'),  # Liste des clients
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),  # Détails d'un client
    path('clients/ajouter/', views.client_add, name='client_add'),  # Ajouter un client
    path('clients/modifier/<int:client_id>/', views.client_edit, name='client_edit'),  # Modifier un client
    path('clients/supprimer/<int:client_id>/', views.client_delete, name='client_delete'),  # Nouvelle URL pour supprimer un client
    path('clients/<int:client_id>/interactions/ajouter/', views.ajouter_interaction, name='ajouter_interaction'),


]
