# Generated by Django 5.1.1 on 2024-09-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0010_alter_blog_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="cover_image",
            field=models.ImageField(blank=True, null=True, upload_to="covers/"),
        ),
    ]