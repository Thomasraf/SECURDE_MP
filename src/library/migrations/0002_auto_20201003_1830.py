# Generated by Django 3.0.5 on 2020-10-03 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookborrow',
            name='date_borrowed',
            field=models.DateField(default=datetime.datetime(2020, 10, 3, 18, 30, 15, 132589)),
        ),
        migrations.AlterField(
            model_name='bookborrow',
            name='due_back',
            field=models.DateField(default=datetime.datetime(2020, 10, 18, 18, 30, 15, 132589)),
        ),
    ]