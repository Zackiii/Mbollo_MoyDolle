from django.urls import path
from messaging import views



urlpatterns = [

path('chat', views.chat, name="chat"),


]