# Generated by Django 5.1.1 on 2024-09-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Profile",
            new_name="PasswordReset",
        ),
        migrations.AddField(
            model_name="user",
            name="nickname",
            field=models.CharField(max_length=30, null=True),
        ),
    ]