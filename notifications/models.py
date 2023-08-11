from django.db import models
from django.contrib.auth.models import User
from messaging.models import Message
from django.contrib.auth import get_user_model

User = get_user_model()


class Notification(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='userNotify')
    content = models.ForeignKey(Message, on_delete=models.CASCADE)
    notification = models.TextField(max_length=100)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
