# Generated by Django 5.1 on 2024-09-05 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("search", "0003_rename_body_question_content_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Question",
        ),
    ]
