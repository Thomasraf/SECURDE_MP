from django.shortcuts import render

# Create your views here.

book = [
    {
        'title': 'How to fly to the sun',
        'author': 'Rafael Cruz',
        'yearOfPublication': 'June 11, 1998',
        'isbn': '1234567890',
        'deweyDecimalSystem': '123'
    },
    {
        'title': 'How to fly to the moon',
        'author': 'Julian De Castro',
        'yearOfPublication': 'March 17, 1998',
        'isbn': '0987654321',
        'deweyDecimalSystem': '321'
    }
]

def home(request):
    context = {
        'book': book
    }
    return render(request, 'books/home.html', context)

def about(request):
    return render(request, 'books/about.html')