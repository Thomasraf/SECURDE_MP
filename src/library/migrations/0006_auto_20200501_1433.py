# Generated by Django 3.0.5 on 2020-05-01 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20200501_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='account',
            name='password2',
        ),
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
