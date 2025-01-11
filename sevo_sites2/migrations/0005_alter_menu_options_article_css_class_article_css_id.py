# Generated by Django 5.1.4 on 2025-01-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sevo_sites2", "0004_menu_alter_article_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="menu",
            options={"verbose_name": "Menu", "verbose_name_plural": "Menus"},
        ),
        migrations.AddField(
            model_name="article",
            name="css_class",
            field=models.CharField(
                blank=True, max_length=500, null=True, verbose_name="CSS Classes"
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="css_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="CSS ID"
            ),
        ),
    ]
