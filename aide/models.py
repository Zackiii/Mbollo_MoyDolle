from django.db import models
from django.contrib.auth.models import User
from user.models import Category, Demandeur


class Aide(models.Model):
    category = models.ForeignKey(
        Category, related_name='categorie', on_delete=models.CASCADE)
    context = models.TextField(max_length=700, blank=True)
    facture = models.FileField(upload_to='DocAide/', null=True, blank=True)
    user = models.ForeignKey(Demandeur, related_name='aides' ,on_delete=models.CASCADE, null=True)
# Create your models here.
