# Generated by Django 4.2 on 2023-06-06 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
        ("aide", "0002_alter_aide_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="aide",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="aides",
                to="user.demandeur",
            ),
        ),
    ]