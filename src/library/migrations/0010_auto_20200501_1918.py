# Generated by Django 3.0.5 on 2020-05-01 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20200501_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='password1',
            new_name='password',
        ),
    ]
