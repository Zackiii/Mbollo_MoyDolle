# Generated by Django 4.1.7 on 2023-05-31 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
        ("aide", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aide",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="categorie",
                to="user.category",
            ),
        ),
    ]
