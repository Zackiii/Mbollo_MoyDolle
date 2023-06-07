from django.shortcuts import render
from .models import Aide
from user.models import Category, Demandeur, Association
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# view pour la recuperation et l'enrengistrement d'une demande


@login_required(login_url='/user_login')
def helping(request):
    categorie = Category.objects.all()
    demandeur = Demandeur.objects.get(user=request.user)
    if request.method == 'POST':
        text = request.POST.get('text')
        devis = request.FILES['thumbnail']

        category_name = request.POST.get('category')
        category = Category.objects.get(name=category_name)

        aide = Aide.objects.create(
            category=category, context=text, facture=devis, user=demandeur)
        aide.save()
        return redirect('accueil')

    context = {
        'categorie': categorie
    }
    return render(request, 'userTests/demande_aide.html', context)


# view pour l'affichage des demandes d'aide pour les demanders
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


# view pour l'affichage des demandes d'aide pour les associations
@login_required
def helpAsking(request):
    association = Association.objects.get(user=request.user)
    category = association.category
    demandes = Aide.objects.filter(category=category)

    context = {
        'demandes': demandes,

    }

    return render(request, 'userTests/helpAsking.html', context)

# Create your views here.
