# Generated by Django 5.1.4 on 2025-01-10 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sevo_sites", "0005_site_order"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="site",
            options={
                "ordering": ["menu_type", "order"],
                "verbose_name": "Site",
                "verbose_name_plural": "Sites",
            },
        ),
        migrations.AddField(
            model_name="site",
            name="subsites",
            field=models.ManyToManyField(blank=True, to="sevo_sites.site"),
        ),
        migrations.AlterField(
            model_name="article",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Created"),
        ),
        migrations.AlterField(
            model_name="article",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated"),
        ),
        migrations.AlterField(
            model_name="site",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Created"),
        ),
        migrations.AlterField(
            model_name="site",
            name="menu_type",
            field=models.CharField(
                choices=[("MAIN", "Main"), ("META", "Meta"), ("NONE", "None")],
                default="Main",
                max_length=10,
                verbose_name="Menu Type",
            ),
        ),
        migrations.AlterField(
            model_name="site",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated"),
        ),
    ]
