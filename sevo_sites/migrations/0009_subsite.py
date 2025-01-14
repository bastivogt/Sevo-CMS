# Generated by Django 5.1.4 on 2025-01-10 22:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sevo_sites", "0008_site_available"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subsite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveIntegerField(default=0)),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="master_site",
                        to="sevo_sites.site",
                    ),
                ),
                (
                    "subsite",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="sub_site",
                        to="sevo_sites.site",
                    ),
                ),
            ],
        ),
    ]
