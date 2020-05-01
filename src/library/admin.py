from django.contrib import admin
from .models import Book, Account

# Register your models here.

admin.site.register(Book)
admin.site.register(Account)