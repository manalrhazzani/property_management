from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm
from biens.models import Bien

# Accueil
def accueil(request):
    return render(request, 'base.html')

# Liste des clients
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

# Détails d'un client
def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'clients/client_detail.html', {'client': client})

# Ajouter un client
def client_add(request, client_id=None):
    biens = Bien.objects.all()  # Récupérer tous les biens
    if request.method == 'POST':
        # Logique pour ajouter un client, ici en utilisant un formulaire ou de manière manuelle
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        telephone = request.POST['telephone']
        type_client = request.POST['type_client']
        bien_id = request.POST.get('bien')  # Récupère l'id du bien, si un bien est sélectionné

        bien = Bien.objects.get(id=bien_id) if bien_id else None  # Si un bien est sélectionné, on le récupère

        client = Client.objects.create(
            nom=nom,
            prenom=prenom,
            email=email,
            telephone=telephone,
            type_client=type_client,
            bien=bien  # Associer le bien choisi
        )
        return redirect('client_list')  # Rediriger vers la liste des clients après l'ajout
    else:
        # Si c'est un GET, afficher le formulaire vide
        return render(request, 'clients/client_form.html', {'biens': biens})
# Modifier un client
def client_edit(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/client_form.html', {'form': form})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client

def client_delete(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'clients/client_delete.html', {'client': client})


from .forms import InteractionForm

def ajouter_interaction(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.client = client  # Associe l'interaction au client
            interaction.save()
            return redirect('client_detail', client_id=client.id)  # Redirige vers la page de détail du client
    else:
        form = InteractionForm()

    return render(request, 'interactions/ajouter_interaction.html', {'form': form, 'client': client})