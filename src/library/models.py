from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    year_of_pub = models.IntegerField()
    ISBN = models.CharField(max_length=17)
    dewey_call = models.CharField(max_length=3)
    reserved = models.BooleanField()
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
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{}-{}'.format(self.book.title, str(self.account.username))