from django.contrib import admin
from django.urls import path, include
from . import views  # Assure-toi que index est bien défini ici
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import set_language
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('', views.index, name='index'),  # ✅ racine vers la page d'accueil intelligente

    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('agent/dashboard/', views.agent_dashboard, name='agent_dashboard'),
    path('client/dashboard/', views.client_dashboard, name='client_dashboard'),

    path('biens/', include('biens.urls')),
    path('clients/', include('clients.urls')),
    path('rendezvous/', include('rendezvous.urls')),
    path('rapports/', include('rapports.urls')),
    path('utilisateurs/', include('utilisateurs.urls')),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 