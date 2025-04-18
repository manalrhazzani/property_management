from django.urls import path
from . import views
app_name = 'rendezvous'

urlpatterns = [
    path('rendezvous/', views.liste_rendezvous, name='liste_rendezvous'),
    path('rendezvous/ajouter/', views.ajouter_rendezvous, name='ajouter_rendezvous'),
    path('rendezvous/modifier/<int:pk>/', views.modifier_rendezvous, name='modifier_rendezvous'),
    path('rendezvous/supprimer/<int:pk>/', views.supprimer_rendezvous, name='supprimer_rendezvous'),
    path('rendezvous/calendrier/', views.calendrier_rendezvous, name='calendrier_rendezvous'),
    path('rendezvous/changer-statut/<int:pk>/<str:nouveau_statut>/', views.changer_statut_rendezvous, name='changer_statut_rdv'),
    path('prendre_rdv/', views.prendre_rdv, name='prendre_rdv'),

    # ✅ Endpoint JSON pour les événements du calendrier
    path('rendezvous/json/', views.rendezvous, name='rendezvous_json'),
]
