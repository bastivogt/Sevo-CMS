# Generated by Django 5.1.4 on 2025-01-11 19:41

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("sevo_media", "0005_alter_filetag_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
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
                (
                    "title",
                    models.CharField(max_length=255, unique=True, verbose_name="Title"),
                ),
                ("content", tinymce.models.HTMLField(verbose_name="Content")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Site2",
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
                (
                    "title",
                    models.CharField(max_length=50, unique=True, verbose_name="Title"),
                ),
                (
                    "slug",
                    models.SlugField(max_length=100, unique=True, verbose_name="Slug"),
                ),
                (
                    "order",
                    models.PositiveBigIntegerField(default=0, verbose_name="Order"),
                ),
                (
                    "meta_keywords",
                    models.TextField(
                        blank=True,
                        max_length=160,
                        null=True,
                        verbose_name="Meta Keywords",
                    ),
                ),
                (
                    "meta_description",
                    models.TextField(
                        blank=True,
                        max_length=160,
                        null=True,
                        verbose_name="Meta Description",
                    ),
                ),
                (
                    "url_path",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="URL Path"
                    ),
                ),
                (
                    "is_reverse",
                    models.BooleanField(default=False, verbose_name="Is Reverse"),
                ),
                (
                    "published",
                    models.BooleanField(default=True, verbose_name="Published"),
                ),
                ("is_home", models.BooleanField(default=False, verbose_name="Is Home")),
                ("available", models.BooleanField(default=True)),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
                (
                    "picture",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="sevo_media.picture",
                        verbose_name="Picture",
                    ),
                ),
            ],
            options={
                "verbose_name": "Site2",
                "verbose_name_plural": "Sites2",
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="Site2Article",
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
                    "article",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="sevo_sites2.article",
                    ),
                ),
                (
                    "site2",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="sevo_sites2.site2",
                    ),
                ),
            ],
        ),
    ]