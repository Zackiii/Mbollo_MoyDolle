from django.shortcuts import render, redirect
from notifications.models import Notification
from django.contrib.auth.decorators import login_required


# Vue montrant les notifications 
@login_required
def DisplayNotifications(request):
    user = request.user
    notifications = Notification.objects.filter(user = user, is_read=False).order_by('date')


    context = {

        'notifications' :  notifications
    }

    return render(request, 'userTests/notifications.html', context)

# Fin du view -------------


# Vue qui supprime une notification
@login_required
def DeleteNotification(request, noti_id):
    user = request.user
    Notification.objects.filter(id=noti_id, user=user).delete()
    Notification.objects.filter(id=noti_id, user=user).update(is_read=True)
    return redirect('DisplayNotifications')

# Fin du view -------------


# Vue qui compte le nombre de notification
@login_required
def CountNotifications(request):
    count_notifications = None
    if request.user.is_authenticated:
        count_notifications = Notification.objects.filter(user=request.user, is_read=False).count()
    return {'count_notifications': count_notifications}

# Fin du view -------------