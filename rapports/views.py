from django.shortcuts import render

# Vue pour afficher la liste des rapports
def rapports_list(request):
    return render(request, 'rapports/list.html')  # Assure-toi que ce template existe
