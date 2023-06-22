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
    priseEnCharge = models.ManyToManyField(Association, related_name='supportLike')
    association = models.ForeignKey(Association, on_delete=models.SET_NULL, null=True, blank=True)

    def number_of_likes(self):
        return self.likes.count()
# Create your models here.
