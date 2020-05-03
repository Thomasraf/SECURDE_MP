# Generated by Django 3.0.5 on 2020-05-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_auto_20200501_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('regular', 'Student/Teacher'), ('manager', 'Book Manager'), ('admin', 'Administrator')], default='regular', max_length=200),
        ),
    ]