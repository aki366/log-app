# Generated by Django 5.0 on 2023-12-29 18:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="language",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="technology",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
