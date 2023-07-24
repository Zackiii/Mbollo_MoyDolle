from django.db import models
from user.models import Demandeur, Association
from django.contrib.auth.models import User
from django.conf import settings



class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(
       settings.AUTH_USER_MODEL , related_name="receiver", on_delete=models.CASCADE)
    message_content = models.TextField(max_length=9000)
    published_date = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)
    read_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    Isread = models.BooleanField(default=False)

# Create your models here.
