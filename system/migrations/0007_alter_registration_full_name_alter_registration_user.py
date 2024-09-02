# Generated by Django 5.0.7 on 2024-09-01 20:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("system", "0006_registration_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="registration",
            name="full_name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="registration",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="registrations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
