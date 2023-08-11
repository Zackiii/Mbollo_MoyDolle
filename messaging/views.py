from django.shortcuts import get_object_or_404, render, redirect
from user.models import Demandeur, Association, User
from django.contrib.auth.decorators import login_required
from .models import Message
from django.db import models
from django.http import JsonResponse
from notifications.models import Notification


@login_required
def chat(request, receiver_username):
    sender = request.user
    receiver = get_object_or_404(User, username=receiver_username)

    # Récupérer tous les messages entre l'expéditeur et le destinataire, triés par ordre chronologique (les plus récents en premier)
    messages = Message.objects.filter(
        # Messages de l'expéditeur vers le destinataire
        (models.Q(sender=sender) & models.Q(receiver=receiver)) |
        # Messages du destinataire vers l'expéditeur
        (models.Q(sender=receiver) & models.Q(receiver=sender))
    ).order_by('date_created')  # Utilisation de 'date_created' pour trier par ordre chronologique

#Creation d'une notification 
    notif = None 
    
    for message in messages:
        if not message.is_read:
            notif = Notification.objects.create(
                user=sender,
                message=message,
                notification=f'Nouveau message de {sender.username}',
                date=message.date_created
            )
    
    messages.update(is_read=True)


    context = {
        'receiver_username': receiver_username,
        'user': sender,
        'messages': messages,
        'notif': notif,
    }
    return render(request, 'userTests/chat.html', context)

# Fin du view-------------


# Choix de l'association pour entamer une discussion
@login_required
def choiceSender(request):

    current_user = request.user
    associations = Association.objects.exclude(user=current_user)

    return render(request, 'userTests/users_list.html', {'associations': associations})

# Fin du view-------------


# Vue pour verifier les nouveaux messages
@login_required
def get_messages(request, receiver_username):

    sender = request.user
    receiver = User.objects.get(username=receiver_username)

    messages = Message.objects.filter(
        # Messages de l'expéditeur vers le destinataire
        (models.Q(sender=sender, receiver=receiver)) |
        # Messages du destinataire vers l'expéditeur
        (models.Q(sender=receiver, receiver=sender))
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

# Fin du view-------------
