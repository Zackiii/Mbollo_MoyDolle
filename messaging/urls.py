from django.urls import path
from messaging import views
from messaging.views import *


urlpatterns = [

    path('chat/<str:receiver_username>/', views.chat, name="chat"),
    path('choiceSender', views.choiceSender, name='users_list'),
    path('get_messages/<str:receiver_username>/', views.get_messages, name='get_messages'),
    # path('mark_message_as_read/<int:message_id>/', views.mark_message_as_read, name='mark_message_as_read'),

]
