# Generated by Django 5.1.1 on 2024-09-08 05:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0003_alter_chatgroup_teacher"),
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatgroup",
            name="teacher",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="chat_group_relation",
                to="teachers.teacher",
            ),
        ),
    ]
