from django.shortcuts import render
from .models import Aide
from user.models import Category, Demandeur, Association
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/user_login')
def helping(request):
    categorie = Category.objects.all()
    if request.method == 'POST':
        text = request.POST.get('text')
        devis = request.FILES['thumbnail']

        category_name = request.POST.get('category')
        category = Category.objects.get(name=category_name)

        aide = Aide.objects.create(
            category=category, context=text, facture=devis)
        aide.save()
        return redirect('accueil')

    context = {
        'categorie': categorie
    }
    return render(request, 'userTests/demande_aide.html', context)


@login_required
def demande(request):
    categories = Category.objects.all()
    demandeur = Demandeur.objects.get(user=request.user)
    aides = Aide.objects.filter(user=demandeur)

    context = {
        'aides': aides,
        'categories': categories
    }

    return render(request, 'userTests/demande.html', context)


@login_required
def helpAsking(request):
    # Récupérer l'association actuelle
    association = Association.objects.get(user=request.user)
    category = association.category  # Récupérer la catégorie de l'association

    # Filtrer les demandes d'aide par la catégorie de l'association
    demandes = Aide.objects.filter(category=category)

    context = {
        'demandes': demandes
    }

    return render(request, 'userTests/helpAsking.html', context)

# Create your views here.
