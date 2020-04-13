from django.shortcuts import render
from .models import Book

# Create your views here.
books = [
    {
        'title': 'How To Fly To The Sun',
        'author': 'Rafael Cruz',
        'dateOfPublication': 'June 11, 1998'
    },
    {
        'title': 'How To Fly To The Moon',
        'author': 'Julian De Castro',
        'dateOfPublication': 'March 17, 1998'
    }
]


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'library/home.html', context)

def about(request):
    return render(request, 'library/about.html', {'title': 'About'})