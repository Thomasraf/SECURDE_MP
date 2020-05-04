from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, default=None)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    year_of_pub = models.IntegerField()
    description = models.TextField()
    ISBN = models.CharField(max_length=17)
    dewey_call = models.CharField(max_length=3)
    reserved = models.BooleanField(default=False)
    reviews = models.TextField() #needs to be changed
    
    def __str__(self):
        return self.title

class Account(models.Model):

    QUESTION_CHOICES = [
    ('city', 'In what city did you have your first ever birthday party?'),
    ('science', 'What is the last name of your Science class teacher in high school?'),
    ('phone', 'Which company manufactured your first mobile phone?'),
    ('hero', 'Who was your childhood hero?'),
    ('vacation', 'Where was your best family vacation?'),
    ]

    ROLES = [
        ('regular', 'Student/Teacher'),
        ('manager', 'Book Manager'),
        ('admin', 'Administrator'),
    ]

    first_name        = models.CharField(max_length=100, default=None)
    last_name         = models.CharField(max_length=100)
    username          = models.CharField(max_length=100)
    email             = models.EmailField(max_length=150)
    password          = models.CharField(max_length=100)
    id_num            = models.IntegerField()
    role              = models.CharField(max_length=200, choices=ROLES, default='regular')
    security_question = models.CharField(max_length=200, choices=QUESTION_CHOICES, default='city')
    security_answer   = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} ({self.last_name})'

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False, password=None,is_staff, is_superuser, first_name, last_name, username,id_num, role, security_question, security_answer):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not password:
#             raise ValueError("Users must have a password")
#         email   = self.normalize_email(email)
#         user    = self.model(
#             email=email, 
#             is_staff=is_staff,
#             is_superuser=is_superuser,
#             first_name=first_name, 
#             last_name=last_name, 
#             username=username, 
#             id_num=id_num, 
#             role=role, 
#             security_question=security_question, 
#             security_answer=security_answer,
#             )
#         return user

#     def create_staffuser(self,email,password,first_name,last_name,username):
#         user = self.create_user(
#             email,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             is_staff=True,
#         )
#         return user

#     def create_superuser(self,email,password,first_name,last_name,username):
#         user = self.create_user(
#             email,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             is_staff=True,
#             is_admin=True
#         )
#         return user

# class User(AbstractUser, PermissionsMixin):

#     QUESTION_CHOICES = [
#     ('city', 'In what city did you have your first ever birthday party?'),
#     ('science', 'What is the last name of your Science class teacher in high school?'),
#     ('phone', 'Which company manufactured your first mobile phone?'),
#     ('hero', 'Who was your childhood hero?'),
#     ('vacation', 'Where was your best family vacation?'),
#     ]

#     ROLES = [
#         ('regular', 'Student/Teacher'),
#         ('manager', 'Book Manager'),
#         ('admin', 'Administrator'),
#     ]

#     first_name        = models.CharField(max_length=100, default=None)
#     last_name         = models.CharField(max_length=100)
#     username          = models.CharField(max_length=100, unique=True)
#     email             = models.EmailField(max_length=100, unique=True)
#     id_num            = models.IntegerField(unique=True)
#     role              = models.CharField(max_length=200, choices=ROLES, default='regular')
#     security_question = models.CharField(max_length=200, choices=QUESTION_CHOICES, default='city')
#     security_answer   = models.CharField(max_length=200)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'id_num', 'role', 'role','security_question','security_answer']

#     objects = AccountManager()

#     def __str__(self):
#         return f'{self.first_name} ({self.last_name})'

#     @property
#     def is_staff(self):
#         return self.staff
    
#     @property
#     def is_admin(self):
#         return self.admin
    
#     @property
#     def is_active(self):
#         return self.active
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{}-{}'.format(self.book.title, str(self.account.username))