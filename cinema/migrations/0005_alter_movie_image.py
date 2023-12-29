# Generated by Django 4.2.8 on 2023-12-28 14:05

import cinema.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0004_alter_movie_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="image",
            field=models.ImageField(
                null=True, upload_to=cinema.models.movie_image_file_path
            ),
        ),
    ]