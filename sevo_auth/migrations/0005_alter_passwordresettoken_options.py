# Generated by Django 5.1.3 on 2024-11-20 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sevo_auth', '0004_passwordresettoken_done'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='passwordresettoken',
            options={'verbose_name': 'Password Reset Token', 'verbose_name_plural': 'Password Reset Tokens'},
        ),
    ]
