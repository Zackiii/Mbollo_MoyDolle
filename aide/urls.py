from django.urls import path
from aide import views

urlpatterns = [

    path('demande_aide', views.helping, name='demande_aide'),
    path('demande', views.demande, name="demande"),
    path('helpAsking', views.helpAsking, name="helpAsking"),
    path('priseEnCharge/<int:aide_id>',
         views.priseEnCharge, name="priseEnCharge"),
    path('signalerArnaque/<int:aide_id>',
         views.signalerArnaque, name="signalerArnaque"),
    path('dashboard', views.dashboard, name='dashboard'),

]
