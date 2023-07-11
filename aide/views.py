from django.http import HttpResponse
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
# fin du view---------------


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
# fin du view-------------


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
# fin du view-----------


# view pour la prise en charge
def priseEnCharge(request, aide_id):
    if request.method == 'POST':
        aide = Aide.objects.get(id=aide_id)
        aide.association = request.user.association
        aide.support = True
        aide.save()

    return redirect('helpAsking')


def signalerArnaque(request, aide_id):
    if request.method == 'POST':
        aide = Aide.objects.get(id=aide_id)
        aide.signalement_arnaque = request.user.association
        aide.IsArnaque = True
        aide.save()

    return redirect('helpAsking')

# fin du view----------


# view pour le dashboard
@login_required
def dashboard(request):
    association = Association.objects.get(user=request.user)
    category = association.category
    demandes = Aide.objects.filter(category=category)
    nombre_demandes = demandes.count()  # Compter le nombre de demandes
    demandes_prises_en_charge = demandes.filter(
        association=association).count()

    context = {
        'demandes': demandes,
        'association': association,
        # Ajouter le nombre de demandes dans le contexte
        'nombre_demandes': nombre_demandes,
        'nombre_demandes_prises_en_charge': demandes_prises_en_charge,
    }
    return render(request, 'userTests/dashboard.html', context)

# Fin du view ----------------------
