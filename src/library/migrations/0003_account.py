# Generated by Django 3.0.5 on 2020-05-01 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20200414_0531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('password1', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
                ('id_num', models.IntegerField()),
                ('security_question', models.CharField(choices=[('city', 'In what city did you have your first ever birthday party?'), ('science', 'What is the last name of your Science class teacher in high school?'), ('phone', 'Which company manufactured your first mobile phone?'), ('hero', 'Who was your childhood hero?'), ('vacation', 'Where was your best family vacation?')], default='city', max_length=200)),
                ('security_answer', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
    ]