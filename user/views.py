from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from .models import *
from actualite.models import Post
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from user.models import Contact

# Vue de la page d'accueil


def accueil(request):
    posts = Post.objects.all()
    assos = Association.objects.all()
    categorie = Category.objects.all()
    user_id = request.user.id
    context = {
        'posts': posts,
        'assos': assos,
        'categorie': categorie,
    }
    return render(request, 'userTests/accueil.html', context)

# ------------ FIN ---------------

# login for association


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(
                request, 'Veuillez fournir un e-mail et un mot de passe valides.')
            return redirect('user_login')

        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            messages.error(
                request, 'Les informations d\'identification fournies ne sont pas valides.')
            return redirect('user_login')
    # new
    if request.user.is_authenticated:
        return redirect('accueil')

    return render(request, 'userTests/user_login.html', {})


# register for association
def sing_up(request):
    message = ""
    error = False
    categorie = Category.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        numero = request.POST.get('contact', None)
        address = request.POST.get('address', None)
        docRecepiss = request.FILES['docRecepiss']
        # category = request.POST.get('category')
        category_name = request.POST.get('category')
        category = Category.objects.get(name=category_name)

        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)

        print(category)
        # Email
        try:
            validate_email(email)
        except:
            error = True
            message = "Enter un email valide svp!"
        # password
        if error == False:
            if password != repassword:
                error = True
                message = "Les deux mot de passe ne correspondent pas!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"

            # verifcation du recipisse a savoir si c'est un fichier pdf
        if docRecepiss.content_type != 'application/pdf':
            message = 'Le fichier doit être au format PDF.'

        # Vérifie la taille du fichier (ici, on limite à 10MB)
        if docRecepiss.size > 10*1024*1024:
            message = 'Le fichier est trop gros (la taille maximale est de 10 Mo).'

            # register
        if error == False:
            # Create user and association objects
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )
            user.is_association = True
            user.is_active = False
            user.save()

            association = Association.objects.create(
                user=user,
                email=email,
                numero=numero,
                address=address,
                docRecepiss=docRecepiss,
                category=category
                # activitePrincipal=activitePrincipal,
                # activiteSecondaire=activiteSecondaire,
                # activiteThird=activiteThird
            )

            # Login user
            # auth_user = authenticate(request, username=name, password=password)
            # login(request, auth_user)

            messages.success(
                request, "Votre inscription est en cours de validation. Veuillez patienter pour la confirmation de votre compte.")
            return redirect('accueil')

    context = {
        'error': error,
        'message': message,
        'categorie': categorie
    }
    return render(request, 'userTests/register.html', context)


# register for demandeur
def sign_upp(request):
    error = False
    message = ""
    if request.method == 'POST':
        full_name = request.POST.get('fullname', None)
        nomUser = request.POST.get('nomUser', None)
        numero = request.POST.get('contact', None)
        address = request.POST.get('address', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        photoCIN = request.FILES['photo_cni']

        if not error:
            if password != repassword:
                error = True
                message = "Les deux mots de passe ne correspondent pas!"

        if not error:
            # Créer un utilisateur et un objet Demandeur
            user = User.objects.create_user(
                username=nomUser,
                password=password
            )

            user.is_demandeur = True
            user.is_active = False
            user.save()

            demandeur = Demandeur.objects.create(
                user=user,
                full_name=full_name,
                number=numero,
                address=address,
                photoCIN=photoCIN,
            )

            # Connecter l'utilisateur
            # auth_user = authenticate(
            #     request, username=nomUser, password=password)
            # login(request, auth_user)
            messages.success(
                request, "Votre inscription est en cours de validation. Veuillez patienter pour la confirmation de votre compte.")
            return redirect('accueil')

    context = {
        'error': error,
        'message': message,
    }

    return render(request, 'userTests/register2.html', context)

# ---------------Fin-----------------

# login for demander


def user_login2(request):
    if request.method == 'POST':
        nomUser = request.POST.get('nomUser')
        password = request.POST.get('password')
        if not nomUser or not password:
            messages.error(
                request, 'Veuillez fournir un nom utilisateur et un mot de passe valides.')
            return redirect('user_login')

        user = authenticate(request, username=nomUser, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            messages.error(
                request, 'Les informations d\'identification fournies ne sont pas valides.')
            return redirect('user_login')

    if request.user.is_authenticated:
        return redirect('accueil')

    return render(request, 'userTests/user_login2.html', {})

# ---------------Fin-----------------

# deconnexion


def log_out(request):
    logout(request)
    return redirect('accueil')

# ---------------Fin-----------------

# Affichage actualite


def news(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,

    }
    return render(request, 'userTests/news.html', {})
# ---------------Fin-----------------


# Ajouter actualite
@login_required(login_url='/user_login')
def getNews(request):
    author = request.user
    posts = Post
    if request.method == "POST":
        title = request.POST['titre']
        text = request.POST['text']
        thumbnail = request.FILES['thumbnail']

        posts = Post.objects.create(
            title=title, text=text, thumbnail=thumbnail, author=author)

        posts.save()

    return redirect('/')
# ---------------Fin-----------------

# supprimer actualite @login_required(login_url='/login')


@login_required(login_url='/user_login')
def actu_delete(request, posts_id):
    posts_id = int(posts_id)
    try:
        posts = Post.objects.get(id=posts_id)
    except Post.DoesNotExist:
        return redirect('accueil')
    posts.delete()
    return redirect('accueil')
# ---------------Fin-----------------

# @login_required(login_url='/user_login')
# def deleteConfirm(request, post_id):
#     post = Post.objects.get(id=post_id)
#     context = {'post': post}
#     if request.method == "POST":
#         post.delete()
#         return redirect('accueil')
#     return render(request, 'accueil', context)


@login_required(login_url='/user_login')
def update(request, post_id):
    posts = Post.objects.get(id=post_id)
    context = {
        'posts': posts, }

    return render(request, 'userTests/updateActu.html', context)


# Update actu
@login_required(login_url='/user_login')
def updateActu(request, post_id):
    post_id = int(post_id)
    posts = Post.objects.get(id=post_id)

    if request.method == 'POST':
        title = request.POST['titre']
        text = request.POST['text']
        thumbnail = posts.thumbnail
        if 'thumbnail' in request.FILES:
            thumbnail = request.FILES['thumbnail']
        posts.title = title
        posts.text = text
        posts.thumbnail = thumbnail
        posts.save()
        return redirect('accueil')

    context = {
        'posts': posts,
    }
    return render(request, 'userTests/accueil.html', context)

# ---------------Fin-----------------

# Search Bar
# def searchEtiquette(request):
#     etiquette = request.GET.get('search')
#     result = Association.objects.filter(Q(activitePrincipal__icontains=etiquette) & Q(
#         activiteSecondaire__icontains=etiquette) & Q(activiteThird__icontains=etiquette)).order_by('-activitePrincipal', '-activiteSecondaire', '-activiteThird')

# def searchEtiquette(request):
#     etiquette = request.GET.get('search')
#     result = Association.objects.filter(
#         Q(user__username__icontains=etiquette) | Q(
#             category__icontains=etiquette)
  #  )
    # .annotate(
    #     priority=Case(
    #         When(category__icontains=etiquette, then=Value(1)),
    #         When(user__username__contains=etiquette, then=Value(2)),
    #         # When(activiteSecondaire__icontains=etiquette, then=Value(3)),
    #         # When(activiteThird__icontains=etiquette, then=Value(4)),
    #         output_field=CharField(),
    #     )
    # ).order_by('priority')

# def seachEtiquette(request):
#     etiquette = request.GET.get('search')
#     result = Association.objects.filter(Q(user__icontains=etiquette)|Q(category__icontains=etiquette))
#     context = {
#         'etiquette': etiquette,
#         'result': result
#     }
#     return render(request, 'userTests/searchView.html', context)


# Search Association
def searchEtiquette(request):
    search_query = request.GET.get('search')
    associations = Association.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    if search_query:
        associations = associations.filter(
            Q(user__username__icontains=search_query) |
            Q(category__name__icontains=search_query) |
            Q(category__subcategories__name__icontains=search_query)
        ).distinct

    context = {
        'associations': associations,
        'categories': categories,
        'subcategories': subcategories,
        'search_query': search_query
    }

    return render(request, 'userTests/searchView.html', context)

# ---------------Fin-----------------

# Voir une actualite full


def post_detail(request, post_id):
    post_id = int(post_id)
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'userTests/post_details.html', context)

# ---------------Fin-----------------

# Page de tout les associations


def associations(request):
    assos = Association.objects.all()
    category = Category.objects.all()
    context = {

        'assos': assos,
        'category': category
    }

    return render(request, 'userTests/associations.html', context)

# ---------------Fin-----------------


def actu(request):
    actu = Post.objects.all()

    context = {

        'actu': actu
    }

    return render(request, 'userTest/actu.html', context)


# Modifier profile
@login_required
def edit_profil(request, user_id):

    user_id = request.user.id
    assos = User.objects.get(id=user_id)
    categorie = Category.objects.all()
    user = User.objects.all()

    if request.method == 'POST':

        name = request.POST.get('name', None)
        print(name)
        numero = request.POST.get('contact', None)
        address = request.POST.get('address', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        if photoCIN in request.File:
            photoCIN = request.FILES['docRecepiss']
        
        category = request.POST.get('category')

        if not error:
            if password != repassword:
                error = True
                message = "Les deux mots de passe ne correspondent pas!"

        user.username = name
        assos.numero = numero
        assos.address = address
        assos.user.set_password(password)
        assos.docRecepiss = photoCIN
        assos.category = category


        assos.user.save()
        assos.save()

        return redirect('accueil')

    context = {
        'assos': assos,
        'categorie': categorie,

    }

    return render(request, 'userTests/edit_profil.html', context)

# ---------------Fin-----------------

 #     name = request.POST.get('name', None)
    #     print(name)
    #     email = request.POST.get('email', None)
    #     numero = request.POST.get('contact', None)
    #     address = request.POST.get('address', None)
    #     category_name = request.POST.get('category')
    #     password = request.POST.get('password', None)
    #     repassword = request.POST.get('repassword', None)

    #     if not error:
    #         if password != repassword:
    #             error = True
    #             message = "Les deux mots de passe ne correspondent pas!"

    #     user.username = name
    #     assos.email = email
    #     assos.numero = numero
    #     assos.address = address
    #     assos.category = Category.objects.get(name=category_name)
    #     assos.user.set_password(password)
    #     assos.user.save()
    #     assos.save()
    #     return redirect('accueil')

    # else:
    #     if user.is_demandeur:


# def edit_profil(request):
#     context = {}
#     return render(request, 'userTests/edit_profil.html', context)


# Toutes les demandes d'aides
def helping(request):
    categorie = Category.objects.all()
    context = {
        'categorie': categorie
    }
    return render(request, 'userTests/demande_aide.html', context)

# ---------------Fin-----------------


# Formulaire de Contact
def contact(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        number = request.POST.get('numero')
        content = request.POST.get('message')

        contact_entry = Contact.objects.create(
            firstName=first_name,
            lastName=last_name,
            email=email,
            number=number,
            content=content
        )
        contact_entry.save()

        subject = 'Mbollo Moy Dolle Confirmation de reception de votre message de Contact'
        message = f"Bonjour {first_name}, \n\nNous avons bien recu votre message, une reponse vous sera communiqué prochainement. \n\nMerci..."
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)
    

        return JsonResponse({'success': True, 'message': 'Message envoyé avec succès.'})

    return redirect('accueil')

# ---------------Fin-----------------
