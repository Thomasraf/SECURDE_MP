# Generated by Django 3.0.5 on 2020-05-07 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(default=None, max_length=200)),
                ('publisher', models.CharField(max_length=100)),
                ('year_of_pub', models.IntegerField()),
                ('description', models.TextField(max_length=1000)),
                ('ISBN', models.CharField(max_length=13)),
                ('dewey_call', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='BookBorrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=200)),
                ('author', models.CharField(default=None, max_length=200)),
                ('publisher', models.CharField(default=None, max_length=100)),
                ('year_of_pub', models.IntegerField(default=None)),
                ('description', models.TextField(default=None, max_length=1000)),
                ('ISBN', models.CharField(default=None, max_length=13)),
                ('dewey_call', models.CharField(default=None, max_length=3)),
                ('userBorrowing', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=200)),
                ('userWhoCommented', models.CharField(default=None, max_length=200)),
                ('content', models.TextField(max_length=280)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Book availability', max_length=1)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.Book')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(default=None, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('id_num', models.IntegerField(unique=True)),
                ('role', models.CharField(choices=[('regular', 'Student/Teacher'), ('manager', 'Book Manager'), ('admin', 'Administrator')], default='regular', max_length=200)),
                ('security_question', models.CharField(choices=[('city', 'In what city did you have your first ever birthday party?'), ('science', 'What is the last name of your Science class teacher in high school?'), ('phone', 'Which company manufactured your first mobile phone?'), ('hero', 'Who was your childhood hero?'), ('vacation', 'Where was your best family vacation?')], default='city', max_length=200)),
                ('security_answer', models.CharField(max_length=200)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
