# Generated by Django 5.1.1 on 2024-09-15 08:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="chatgroup",
            name="members",
            field=models.ManyToManyField(
                blank=True, related_name="chat_group", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]