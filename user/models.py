from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_association = models.BooleanField(default=False)
    is_demandeur = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_autre = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Association(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
   # user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True, null=True)
    numero = models.TextField(max_length=100, blank=True, null=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    docRecepiss = models.FileField(
        upload_to='VerifyDocument/', null=True, blank=True)
    # category = models.ManyToManyField(unique=True, null=True,on_delete=models.CASCADE, primary_key=True)
    category = models.ForeignKey(
        Category, related_name='categoryLink', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.user.username, self.address)


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name


class Demandeur(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=100, blank=True)
    nomUser = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    number = models.TextField(max_length=100, blank=True, null=True)
    photoCIN = models.FileField(upload_to='PhotoCIN/', null=True, blank=True)

    def __str__(self):
        return self.full_name

# Create your models here.
