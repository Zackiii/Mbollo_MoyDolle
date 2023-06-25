from django.urls import path
from aide import views
from aide.views import *

urlpatterns = [

    path('demande_aide', helping, name='demande_aide'),
    path('demande', demande, name="demande"),
    path('helpAsking', helpAsking, name="helpAsking"),
    path('priseEnCharge/<int:aide_id>',
         views.priseEnCharge, name="priseEnCharge"),
    path('dashboard', views.dashboard, name='dashboard'),

]
