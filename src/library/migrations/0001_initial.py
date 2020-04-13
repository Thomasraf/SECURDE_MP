# Generated by Django 3.0.5 on 2020-04-13 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=100)),
                ('year_or_pub', models.IntegerField()),
                ('ISBN', models.CharField(max_length=17)),
                ('dewey_call', models.CharField(max_length=3)),
                ('reserved', models.BooleanField()),
                ('reviews', models.TextField()),
            ],
        ),
    ]