from django.urls import path
from notifications.views import *


urlpatterns = [
    path('', DisplayNotifications, name='DisplayNotifications'),
    path('<noti_id>/delete', DeleteNotification, name='delete-notification')
]