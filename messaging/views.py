from django.shortcuts import get_object_or_404, render, redirect
from user.models import Demandeur, Association, User
from django.contrib.auth.decorators import login_required
from .models import Message


@login_required
def chat(request, user_id):
    receiver = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        message_content = request.POST.get('message_content')
        sender = request.user
        message = Message.objects.create(
            sender=sender, receiver=receiver, message_content=message_content)

    # Récupérer tous les messages entre l'utilisateur connecté et le destinataire
    messages = Message.objects.filter(sender=request.user, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=request.user)

    return render(request, 'userTests/chat.html', {'receiver': receiver, 'messages': messages})



@login_required
def create_message(request):
    if request.method == 'POST':
        receiver_id = request.POST.get('receiver_id')
        message_content = request.POST.get('message_content')
        sender = request.user
        receiver = User.objects.get(id=receiver_id)
        message = Message.objects.create(
            sender=sender, receiver=receiver, message_content=message_content)

    else:

        receivers = User.objects.exclude(id=request.user.id).filter(is_association = True)
        return render(request, 'userTests/create_message.html', {'receivers': receivers})


@login_required
def choiceSender(request):

    current_user = request.user
    users = Association.objects.exclude(user=current_user)

    return render(request, 'userTests/users_list.html', {'users': users})


# def room(request, user_id):

#     sender = request.user
#     receiver = get_object_or_404(User, id=user_id)

#     # room = Association.objects.get(receiver= user_id)
#     message = Message.objects.filter(room=room)[0:30]
#     return render(request, 'userTests/chat.html', {"room": room, 'message': message})

# Create your views here.
