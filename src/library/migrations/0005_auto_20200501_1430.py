# Generated by Django 3.0.5 on 2020-05-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20200501_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='password1',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='account',
            name='password2',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]