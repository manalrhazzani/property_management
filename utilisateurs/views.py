from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from .forms import CustomUserCreationForm
from .models import DemandeAgent, User
from biens.models import Bien
from rendezvous.models import RendezVous
 

def index_view(request):
    return render(request, 'index.html')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # L'utilisateur est déjà enregistré avec le rôle par défaut
            login(request, user)  # Connexion de l'utilisateur

            # Redirection basée sur le rôle
            if user.is_admin:
                return redirect('admin_dashboard')
            elif user.is_agent:
                return redirect('agent_dashboard')
            return redirect('client_dashboard')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        if user.is_admin:
            return reverse('admin_dashboard')
        elif user.is_agent:
            return reverse('agent_dashboard')
        elif user.is_client:
            return reverse('client_dashboard')
        return reverse('index')


@login_required
def client_dashboard(request):
    if not request.user.is_client:
        return redirect('access_denied')
    return render(request, 'dashboards/client/dashboard.html', {
        'user': request.user,
        'title': _('Tableau de bord client')
    })


@login_required
def agent_dashboard(request):
    if not request.user.is_agent:
        return redirect('access_denied')
    
    mes_biens = Bien.objects.filter(agent=request.user)
    rdvs = RendezVous.objects.filter(agent=request.user)
    return render(request, 'dashboards/agent/dashboard.html', {
        'mes_biens': mes_biens,
        'rdvs': rdvs
    })


@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        return redirect('access_denied')

    stats = {
        'total_users': User.objects.count(),
        'new_requests': DemandeAgent.objects.filter(statut='en_attente').count()
    }
    return render(request, 'dashboards/admin/dashboard.html', {
        'stats': stats
    })


def logout_view(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('index')


def access_denied(request):
    if not request.user.is_admin:
        return redirect('access_denied')

    stats = {
        'total_users': User.objects.count(),
        'new_requests': DemandeAgent.objects.filter(statut='en_attente').count()
    }
    return render(request, 'dashboards/admin/dashboard.html', {
        'stats': stats
    })