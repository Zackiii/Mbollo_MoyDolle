# Generated by Django 4.1.7 on 2023-08-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_remove_association_is_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fistName", models.CharField(blank=True, max_length=100)),
                ("lastName", models.CharField(blank=True, max_length=100)),
                ("email", models.EmailField(blank=True, max_length=80, unique=True)),
                ("number", models.TextField(max_length=20)),
                ("content", models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
