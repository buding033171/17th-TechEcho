# Generated by Django 5.1.1 on 2024-09-11 09:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("answers", "0001_initial"),
        ("questions", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="questions.question"
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="vote",
            name="answer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="answers.answer"
            ),
        ),
        migrations.AddField(
            model_name="vote",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterUniqueTogether(
            name="vote",
            unique_together={("user", "answer")},
        ),
    ]