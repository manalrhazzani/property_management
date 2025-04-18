from django.shortcuts import render, redirect, get_object_or_404

from clients.models import Client
from .models import RendezVous
from .forms import PrendreRendezVousForm, RendezVousForm
from django.http import JsonResponse
app_name = 'rendezvous'


def liste_rendezvous(request):
    rendezvous = RendezVous.objects.all()
    return render(request, 'rendezvous/liste_rv.html', {'rendezvous': rendezvous})

def ajouter_rendezvous(request):
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_rendezvous')
    else:
        form = RendezVousForm()
    return render(request, 'rendezvous/ajouter.html', {'form': form})


def modifier_rendezvous(request, pk):
    rv = get_object_or_404(RendezVous, pk=pk)
    if request.method == 'POST':
        form = RendezVousForm(request.POST, instance=rv)
        if form.is_valid():
            form.save()
            return redirect('liste_rendezvous')
    else:
        form = RendezVousForm(instance=rv)
    return render(request, 'rendezvous/modifier.html', {'form': form})

def supprimer_rendezvous(request, pk):
    rv = get_object_or_404(RendezVous, pk=pk)
    rv.delete()
    return redirect('liste_rendezvous')

# Affiche la page contenant le calendrier
def calendrier_rendezvous(request):
    rendezvous = RendezVous.objects.filter(statut='Prévu')
    context = {
        "rendezvous": rendezvous,
    }
    return render(request, 'rendezvous/calendrier.html', context)

# Vue qui retourne les rendez-vous au format JSON
def rendezvous(request):
    rendezvous = RendezVous.objects.filter(statut='Prévu')
    out = []
    for rv in rendezvous:
        out.append({
            "title": f"{rv.client.nom} - {rv.bien.titre}",
            "start": f"{rv.date}T{rv.heure}",
            "description": rv.commentaire,
            "allDay": False
        })
    return JsonResponse(out, safe=False)


from django.contrib import messages

def changer_statut_rendezvous(request, pk, nouveau_statut):
    rdv = get_object_or_404(RendezVous, pk=pk)
    if nouveau_statut in ['Réalisé', 'Annulé']:
        rdv.statut = nouveau_statut
        rdv.save()
        messages.success(request, f"Le rendez-vous a été marqué comme {nouveau_statut.lower()}.")
    return redirect('liste_rendezvous')

# rendezvous/views.py

from django.shortcuts import render, redirect
from .forms import PrendreRendezVousForm
from django.contrib.auth.decorators import login_required


from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import PrendreRendezVousForm
from clients.models import Client
from django.contrib.auth.decorators import login_required

@login_required
def prendre_rdv(request):
    try:
        # Récupérer le client associé à l'utilisateur connecté
        client = Client.objects.get(user=request.user)
    except Client.DoesNotExist:
        # Si aucun profil client n'est trouvé
        messages.error(request, "Aucun profil client associé à cet utilisateur.")
        return redirect('client_dashboard')

    # Vérification du rôle de l'utilisateur
    if not request.user.is_client:
        messages.error(request, "Vous devez être un client pour prendre un rendez-vous.")
        return redirect('client_dashboard')

    if request.method == 'POST':
        form = PrendreRendezVousForm(request.POST)
        if form.is_valid():
            # Créer le rendez-vous associé au client
            rdv = form.save(commit=False)
            rdv.client = client  # Associer le rendez-vous au client
            rdv.statut = 'Prévu'  # Par défaut, le statut est "Prévu"
            rdv.save()
            messages.success(request, "Votre rendez-vous a été pris avec succès.")
            return redirect('client_dashboard')  # Rediriger vers la page d'accueil client
    else:
        form = PrendreRendezVousForm()

    return render(request, 'rendezvous/prendre_rdv.html', {'form': form})