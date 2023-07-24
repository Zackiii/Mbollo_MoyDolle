from django.urls import path
from messaging import views
from messaging.views import *


urlpatterns = [

    path('chat/<int:user_id>', views.chat, name="chat"),
    path('create_message', views.create_message, name='create_message'),
    path('choiceSender', views.choiceSender, name='users_list'),
    # path("<str:user_id>/", views.room, name="room"),

]
