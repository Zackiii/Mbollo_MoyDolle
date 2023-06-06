from django.urls import path
from aide import views
from aide.views import *

urlpatterns = [

    path('demande_aide', helping, name='demande_aide'),
    path('demande', demande, name="demande"),
    path('helpAsking', helpAsking, name="helpAsking"),
]
