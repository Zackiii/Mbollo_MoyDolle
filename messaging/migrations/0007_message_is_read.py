# Generated by Django 4.1.7 on 2023-08-04 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("messaging", "0006_message_date_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="is_read",
            field=models.BooleanField(default=False),
        ),
    ]
