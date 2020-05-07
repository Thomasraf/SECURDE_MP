from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default=None)
    publisher = models.CharField(max_length=100)
    year_of_pub = models.IntegerField()
    description = models.TextField(max_length=1000)
    ISBN = models.CharField(max_length=13)
    dewey_call = models.CharField(max_length=3)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    
class BookInstance(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        if self.book:
            return '%s (%s)' %(self.id, self.book.title)
        else:
            return '%s (%s)' %(self.id, self.imprint)

class BookBorrow(models.Model):
    title = models.CharField(max_length=200, default=None)
    author = models.CharField(max_length=200, default=None)
    publisher = models.CharField(max_length=100, default=None)
    year_of_pub = models.IntegerField(default=None)
    description = models.TextField(max_length=1000, default=None)
    ISBN = models.CharField(max_length=13, default=None)
    dewey_call = models.CharField(max_length=3, default=None)
    userBorrowing = models.CharField(max_length=200, default=None)

    def __str__(self):
        return f'{self.title} ({self.userBorrowing})'

# class BookReturn(models.Model):
#     title = models.CharField(max_length=200, default=None)
#     author = models.CharField(max_length=200, default=None)
#     publisher = models.CharField(max_length=100, default=None)
#     year_of_pub = models.IntegerField(default=None)
#     description = models.TextField(max_length=1000, default=None)
#     ISBN = models.CharField(max_length=13, default=None)
#     dewey_call = models.CharField(max_length=3, default=None)
#     userReturned = models.CharField(max_length=200, default=None)

#     def __str__(self):
#         return f'{self.title} ({self.userReturned})'

class Review(models.Model):
    title = models.CharField(max_length=200, default=None)
    userWhoCommented = models.CharField(max_length=200, default=None)
    content = models.TextField(max_length=280)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f'{self.title} ({self.userWhoCommented})' 
    

    
class UserManager(BaseUserManager):
    def create_user(self, email,first_name,last_name,id_num,role,security_question,security_answer,username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a First Name")
        if not last_name:
            raise ValueError("Users must have a Last Name")
        if not id_num:
            raise ValueError("Users must have an I.D. Number")
        if not role:
            raise ValueError("Users must have a role")
        if not security_question:
            raise ValueError("Users must choose a Security Question")
        if not security_answer:
            raise ValueError("Users must answer their chosen Security Question")
        if not username:
            raise ValueError("Users must have a Username")

        user = self.model(
            email               = self.normalize_email(email),
            first_name          = first_name,
            last_name           = last_name,
            id_num              = id_num,
            role                = role,
            security_question   = security_question,
            security_answer     = security_answer,
            username            = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,first_name,last_name,id_num,role,security_question,security_answer,username, password):
        user = self.create_user(
            email               = self.normalize_email(email),
            first_name          = first_name,
            last_name           = last_name,
            id_num              = id_num,
            role                = role,
            security_question   = security_question,
            security_answer     = security_answer,
            username            = username,
            password            = password,
        )
        user.is_admin       = True
        user.is_staff       = True
        user.is_superuser   = True
        user.save(using=self._db)
        return

class User(AbstractUser):

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
    username          = models.CharField(max_length=100, unique=True)
    email             = models.EmailField(max_length=100, unique=True)
    id_num            = models.IntegerField(unique=True)
    role              = models.CharField(max_length=200, choices=ROLES, default='regular')
    security_question = models.CharField(max_length=200, choices=QUESTION_CHOICES, default='city')
    security_answer   = models.CharField(max_length=200)
    date_joined       = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login        = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin          = models.BooleanField(default=False)
    is_active         = models.BooleanField(default=True)
    is_staff          = models.BooleanField(default=False)
    is_superuser      = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name','id_num','role','security_question','security_answer','email']

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} ({self.last_name})'

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True