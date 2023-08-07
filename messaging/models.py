from django.db import models
from user.models import Demandeur, Association
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(
        User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        User, related_name="received_messages", on_delete=models.CASCADE)
    message_content = models.TextField(max_length=9000)
    date_created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


    

