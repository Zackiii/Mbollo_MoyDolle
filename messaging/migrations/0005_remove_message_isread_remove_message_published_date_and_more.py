# Generated by Django 4.1.7 on 2023-07-26 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "messaging",
            "0004_alter_message_message_content_alter_message_receiver_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="Isread",
        ),
        migrations.RemoveField(
            model_name="message",
            name="published_date",
        ),
        migrations.RemoveField(
            model_name="message",
            name="read_at",
        ),
    ]
