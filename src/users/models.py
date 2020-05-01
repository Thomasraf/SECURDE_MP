from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

# Create your models here.
# class Accounts(models.Model):

#     QUESTION_CHOICES = [
#     ('city', 'In what city did you have your first ever birthday party?'),
#     ('science', 'What is the last name of your Science class teacher in high school?'),
#     ('phone', 'Which company manufactured your first mobile phone?'),
#     ('hero', 'Who was your childhood hero?'),
#     ('vacation', 'Where was your best family vacation?'),
#     ]

#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=150)
#     # password1 = models.CharField(max_length=100)
#     # password2 = models.CharField(max_length=100)
#     id_num = models.IntegerField()
#     security_question = models.CharField(max_length=200, choices=QUESTION_CHOICES, default='city')
#     security_answer = models.CharField(max_length=200)

#     class Meta:
#         ordering = ['first_name', 'last_name']

#     def __str__(self):
#         return f'{self.first_name} ({self.last_name})'