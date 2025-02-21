# Generated by Django 5.1.4 on 2025-01-10 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sevo_sites", "0010_rename_site_subsite_mastersite"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subsite",
            name="subsite",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sub_sites",
                to="sevo_sites.site",
            ),
        ),
    ]
