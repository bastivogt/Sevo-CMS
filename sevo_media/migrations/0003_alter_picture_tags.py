# Generated by Django 5.1.3 on 2024-11-19 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevo_media', '0002_rename_imagetag_picturetag_alter_picture_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='tags',
            field=models.ManyToManyField(blank=True, to='sevo_media.picturetag'),
        ),
    ]
