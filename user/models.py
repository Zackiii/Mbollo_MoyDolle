from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.dispatch import receiver
# from django.db.models.signals import post_save


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
    email = models.EmailField(max_length=254, unique=True, null=True)
    numero = models.TextField(max_length=100, blank=True, null=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    docRecepiss = models.FileField(
        upload_to='VerifyDocument/', null=True, blank=True)
    # category = models.ManyToManyField(unique=True, null=True,on_delete=models.CASCADE, primary_key=True)
    category = models.ForeignKey(
        Category, related_name='categoryLink', on_delete=models.CASCADE)


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


# Create your models here.
