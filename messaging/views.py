from django.shortcuts import get_object_or_404, render, redirect
from user.models import Demandeur, Association, User
from django.contrib.auth.decorators import login_required
from .models import Message


@login_required
def chat(request, receiver_username):

    context = {
        'receiver_username': receiver_username,
        'user': request.user,
    }
    return render(request, 'userTests/chat.html', context)
  



@login_required
def choiceSender(request):

    current_user = request.user
    associations = Association.objects.exclude(user=current_user)

    return render(request, 'userTests/users_list.html', {'associations': associations})


