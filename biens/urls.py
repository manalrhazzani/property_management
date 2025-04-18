from django.urls import path
from . import views
app_name = 'biens'
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('liste/', views.liste_biens, name='liste_biens'),
    path('liste_client/', views.liste_biens_client, name='liste_biens_client'),
    path('favoris/', views.mes_favoris, name='mes_favoris'),
    path('bien/<int:id>/', views.detail_bien, name='detail_bien'),

    path('ajouter/', views.ajouter_bien, name='ajouter_bien'),
    path('modifier/<int:bien_id>/', views.modifier_bien, name='modifier_bien'),
    path('supprimer/<int:bien_id>/', views.supprimer_bien, name='supprimer_bien'),
    path('recherche/', views.recherche_biens_client, name='recherche_biens_client'),
 
]

# Ajout des fichiers médias si DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
