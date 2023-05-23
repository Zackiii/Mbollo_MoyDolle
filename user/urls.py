from django.urls import path
from user import views
from user.views import *


urlpatterns = [
    # path('', dashboard, name='dashboard'),
    path('', accueil, name='accueil'),
    path('user_login', user_login, name='user_login'),
    path('register', sing_up, name='register'),
    path('logout', log_out, name='logout'),
    path('news', news, name='news'),
    path('getNews', views.getNews, name="getNews"),
    path('actu_delete/<int:posts_id>', views.actu_delete, name="actu_delete"),
    path('update/<int:post_id>', views.update, name='update'),
    path('updateActu/<int:post_id>', views.updateActu, name="updateActu"),
    path('searchEtiquette', searchEtiquette, name="searchEtiquette"),
    path('post_details/<int:post_id>', views.post_detail, name="post_details"),
    path('associations', views.associations, name="associations"),
    path('actu', views.actu, name="actu"),
    # path('edit_profil/<int:assos_id>', views.edit_profil, name="edit_profil"),
    # path('deleteConfirm/<int:posts_id>',deleteConfirm, name="deleteConfirm"),

]
