# Generated by Django 4.1.7 on 2023-08-10 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0002_alter_notification_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="notification",
            old_name="message",
            new_name="content",
        ),
    ]
