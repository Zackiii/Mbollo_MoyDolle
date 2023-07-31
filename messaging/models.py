from django.db import models
from user.models import Demandeur, Association
from django.contrib.auth.models import User
from django.conf import settings

class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="received_messages", on_delete=models.CASCADE)
    message_content = models.TextField(max_length=9000)
    date_created = models.DateTimeField(auto_now_add=True)

