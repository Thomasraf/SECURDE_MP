from django.contrib import admin
from .models import Book, BookInstance, User, Review, BookBorrow
# Register your models here.

admin.site.register(Book)
admin.site.register(BookBorrow)
# admin.site.register(BookReturn)
admin.site.register(User)
admin.site.register(Review)
#admin.site.register(Author)
admin.site.register(BookInstance)
#admin.site.register(Genre)