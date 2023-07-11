from django.db import models
from django.contrib.auth.models import User
from user.models import Category, Demandeur, Association


class Aide(models.Model):
    category = models.ForeignKey(
        Category, related_name='categorie', on_delete=models.CASCADE)
    context = models.TextField(max_length=700, blank=True)
    facture = models.FileField(upload_to='DocAide/', null=True, blank=True)
    user = models.ForeignKey(
        Demandeur, related_name='aides', on_delete=models.CASCADE)
    support = models.BooleanField(default=False)
    IsArnaque = models.BooleanField(default=False)
    association = models.ForeignKey(
        Association, on_delete=models.SET_NULL, null=True, blank=True)

# Create your models here.
