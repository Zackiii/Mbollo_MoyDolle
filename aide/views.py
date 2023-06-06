from django.shortcuts import render
from .models import Aide
from user.models import Category
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
    categorie = Category.objects.all()
    aide = Aide.objects.all()

    context = {
        'aide': aide,
        'categorie': categorie
    }

    return render(request, 'userTests/demande.html', context)

# Create your views here.
