# Generated by Django 4.2.8 on 2023-12-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="image",
            field=models.ImageField(null=True, upload_to="movie_image_file_path"),
        ),
    ]