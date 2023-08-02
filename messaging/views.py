from django.shortcuts import get_object_or_404, render, redirect
from user.models import Demandeur, Association, User
from django.contrib.auth.decorators import login_required
from .models import Message
from django.db import models
from django.http import JsonResponse


@login_required
def chat(request, receiver_username):
    sender = request.user
    receiver = get_object_or_404(User, username=receiver_username)

    # Récupérer tous les messages entre l'expéditeur et le destinataire, triés par ordre chronologique (les plus récents en premier)
    messages = Message.objects.filter(
        (models.Q(sender=sender) & models.Q(receiver=receiver)) |  # Messages de l'expéditeur vers le destinataire
        (models.Q(sender=receiver) & models.Q(receiver=sender))  # Messages du destinataire vers l'expéditeur
    ).order_by('date_created')  # Utilisation de 'date_created' pour trier par ordre chronologique

    context = {
        'receiver_username': receiver_username,
        'user': sender,
        'messages': messages,
    }
    return render(request, 'userTests/chat.html', context)
  



@login_required
def choiceSender(request):

    current_user = request.user
    associations = Association.objects.exclude(user=current_user)

    return render(request, 'userTests/users_list.html', {'associations': associations})


def get_messages(request, receiver_username):
    # Récupérer les messages pour le destinataire spécifié
    # Vous pouvez ajuster cette logique en fonction de votre modèle Message
    # Par exemple, pour récupérer les messages liés à l'utilisateur courant (request.user) et au destinataire spécifié

    sender = request.user
    receiver = User.objects.get(username=receiver_username)

    messages = Message.objects.filter(
        (models.Q(sender=sender, receiver=receiver)) |  # Messages de l'expéditeur vers le destinataire
        (models.Q(sender=receiver, receiver=sender))  # Messages du destinataire vers l'expéditeur
    ).order_by('date_created')  # Tri par ordre chronologique

    # Créez une liste pour stocker les messages sous forme de dictionnaires
    messages_list = []
    for message in messages:
        messages_list.append({
            'sender': message.sender.username,
            'message_content': message.message_content,
        })

    # Renvoyer les messages au format JSON
    return JsonResponse({'messages': messages_list})