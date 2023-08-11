from django.http import HttpResponse
from django.shortcuts import render
from .models import Aide
from user.models import Category, Demandeur, Association
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from notifications.models import Notification


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

        # Créer une notification pour la demande faite
        content = f"Une nouvelle demande d'aide a été faite par {demandeur.user.username}."
        notification = Notification(user=request.user, content=content)
        notification.save()

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


# view pour la prise en charge des demandes
def priseEnCharge(request, aide_id):
    if request.method == 'POST':
        aide = Aide.objects.get(id=aide_id)
        aide.association = request.user.association
        aide.support = True
        aide.save()

          # Créer une notification pour la prise en charge
        content = f"Votre demande d'aide a été prise en charge par {request.user.username}."
        notification = Notification(user=aide.user.user, content=content)
        notification.save()

    return redirect('helpAsking')
# fin du view----------


# view pour demandes signale comme possible arnaque des demandes
def signalerArnaque(request, aide_id):
    if request.method == 'POST':
        aide = Aide.objects.get(id=aide_id)
        aide.signalement_arnaque = request.user.association
        aide.IsArnaque = True
        aide.save()

    return redirect('helpAsking')

# fin du view-----------------


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

# # View pour afficher une notification
# @login_required
# def view_notifications(request):
#     user = request.user
#     notifications = Notification.objects.filter(user=user).order_by('date')
    
#     # Marquer les notifications comme lues
#     unread_notifications = notifications.filter(is_read=False)
#     for notification in unread_notifications:
#         notification.is_read = True
#         notification.save()

#     context = {
#         'notifications': notifications,
#     }
#     return render(request, 'userTests/notifications.html', context)

# # Fin du view ----------------------