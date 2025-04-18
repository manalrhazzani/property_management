from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.rapports_list, name='rapports_list'),  # Exemple pour afficher la liste des rapports
    # Tu peux ajouter d'autres routes ici selon les besoins de l'application rapports
]
