from django.shortcuts import render, redirect, get_object_or_404
from .models import Bien
 
from .forms import BienForm
def accueil(request):
    return render(request, 'base.html')
def liste_biens(request):
    biens = Bien.objects.all()
    return render(request, 'biens/liste_biens.html', {'biens': biens})
def liste_biens_client(request):
    biens = Bien.objects.all()

    ville = request.GET.get('ville')
    type_bien = request.GET.get('type')
    prix_max = request.GET.get('prix_max')

    if ville:
        biens = biens.filter(ville__icontains=ville)
    if type_bien:
        biens = biens.filter(type__iexact=type_bien)
    if prix_max:
        biens = biens.filter(prix__lte=prix_max)

    return render(request, 'biens/liste_biens_client.html', {
        'biens': biens,
        'request': request,
    })
def mes_favoris(request):
    biens = Bien.objects.all()
    return render(request, 'biens/mes_favoris.html', {'biens': biens})
def liste_biens(request):
    biens = Bien.objects.all()
    return render(request, 'biens/liste_biens.html', {'biens': biens})
def ajouter_bien(request):
    if request.method == 'POST':
        form = BienForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_biens')
    else:
        form = BienForm()
    return render(request, 'biens/ajouter_bien.html', {'form': form})

def modifier_bien(request, bien_id):
    bien = get_object_or_404(Bien, id=bien_id)
    form = BienForm(request.POST or None, request.FILES or None, instance=bien)
    if form.is_valid():
        form.save()
        return redirect('liste_biens')
    return render(request, 'biens/modifier_bien.html', {'form': form, 'bien': bien})

def supprimer_bien(request, bien_id):
    bien = get_object_or_404(Bien, id=bien_id)
    bien.delete()
    return redirect('liste_biens')
# views.py

from django.shortcuts import render
from .models import Bien

def recherche_biens(request):
    biens = Bien.objects.all()

    ville = request.GET.get('ville')
    type_bien = request.GET.get('type')
    prix_max = request.GET.get('prix_max')

    if ville:
        biens = biens.filter(adresse__icontains=ville)
    if type_bien:
        biens = biens.filter(type=type_bien)
    if prix_max:
        biens = biens.filter(prix__lte=prix_max)

    return render(request, 'biens/liste_biens.html', {'biens': biens})



def recherche_biens_client(request):
    biens = Bien.objects.all()

    city = request.GET.get('city', '').strip()
    type_bien = request.GET.get('type', '').strip()
    max_price = request.GET.get('max_price', '').strip()
    min_bedrooms = request.GET.get('min_bedrooms', '').strip()

    city = request.GET.get('city', '').strip()
    if city:
        # Remplacement des caractères accentués
        city = city.lower().replace('é', 'e').replace('è', 'e').replace('ê', 'e')
        biens = biens.extra(where=["LOWER(REPLACE(REPLACE(REPLACE(city, 'é', 'e'), 'è', 'e'), 'ê', 'e')) LIKE %s"], params=[f"%{city}%"])


    if type_bien:
        biens = biens.filter(type=type_bien)

    if max_price:
        try:
            max_price = float(max_price)
            biens = biens.filter(price__lte=max_price)
        except ValueError:
            pass

    if min_bedrooms:
        try:
            min_bedrooms = int(min_bedrooms)
            biens = biens.filter(bedroom__gte=min_bedrooms)
        except ValueError:
            pass

    return render(request, 'biens/liste_biens_client.html', {
        'biens': biens,
        'city': city,
        'type_bien': type_bien,
        'max_price': max_price,
        'min_bedrooms': min_bedrooms
    })

 
def detail_bien(request, id):
    bien = get_object_or_404(Bien, id=id)
    return render(request, 'biens/detail_bien.html', {'bien': bien})


def client_dashboard(request):
    biens = Bien.objects.all()[:3]  # Limite à 3 biens
    return render(request, 'biens/client_dashboard.html', {'biens': biens})