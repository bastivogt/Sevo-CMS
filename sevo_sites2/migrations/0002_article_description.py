# Generated by Django 5.1.4 on 2025-01-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sevo_sites2", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="description",
            field=models.TextField(
                blank=True, max_length=255, verbose_name="Description"
            ),
        ),
    ]
