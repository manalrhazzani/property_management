from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from utilisateurs.forms import CustomUserCreationForm  # À créer

User = get_user_model()

# Page d'accueil
def index(request):
    # Affiche toujours la page d'accueil, même si l'utilisateur est connecté
    return render(request, 'index.html')

# Inscription (version personnalisée)
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = User.Role.CLIENT  # Force le rôle Client
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte créé pour {username}!')
            login(request, user)
            request.session.modified = True  # Assurez-vous que la session est bien mise à jour
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Connexion
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        messages.error(request, 'Identifiants invalides')
    return render(request, 'login.html')

# Déconnexion
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')

# Tableaux de bord avec vérification des rôles
@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        messages.error(request, 'Accès non autorisé')
        return redirect('index')
    return render(request, 'dashboards/admin/dashboard.html')

@login_required
def agent_dashboard(request):
    if not request.user.is_agent:
        messages.error(request, 'Accès non autorisé')
        return redirect('index')
    return render(request, 'dashboards/agent/dashboard.html')

@login_required
def client_dashboard(request):
    if not request.user.is_client:
        messages.error(request, 'Accès non autorisé')
        return redirect('index')
    return render(request, 'dashboards/client/dashboard.html')

# Pages statiques
def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')