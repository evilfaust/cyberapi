# Generated by Django 4.2.5 on 2023-11-23 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_rename_role_gamedota2_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamedota2',
            name='assists',
        ),
        migrations.RemoveField(
            model_name='gamedota2',
            name='dead',
        ),
        migrations.RemoveField(
            model_name='gamedota2',
            name='gold',
        ),
        migrations.RemoveField(
            model_name='gamedota2',
            name='kills',
        ),
    ]
