from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Book, Review, BookInstance
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import Q
User = get_user_model()


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

# Book Views
def home(request):
    print(request.session)
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'home.html', context)

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        books = Book.objects.filter(title__icontains=q)
        context = {'query': q, 'books': books}
        template = 'results.html'
    else:
        template = 'home.html'
        context = {
            'books': Book.objects.all()
        }
    return render(request, template, context)

def about(request):
    return render(request, 'about.html  ', {'title': 'About'})

def addBook(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            title = request.POST["title"]
            author = request.POST["author"]
            publisher = request.POST["publisher"]
            year_of_pub = request.POST["year_of_pub"]
            description = request.POST["description"]
            ISBN = request.POST["ISBN"]
            dewey_call = request.POST["dewey_call"]
            BookInstance.objects.create(
                book = Book.objects.create(
                title = title,
                author = author,
                publisher = publisher,
                year_of_pub = year_of_pub,
                description = description,
                ISBN = ISBN,
                dewey_call = dewey_call
            ),
                imprint = 'First Edition',
                id = ISBN,
                due_back = datetime.now()+timedelta(days=7),
                status = 'a'
            )
            return redirect('library-home')
    else:
        form = AddBookForm()
    return render(request, "addBook.html", {'form': form})

def viewBook(request, ISBN):
    book = Book.objects.filter(ISBN=ISBN)
    details = get_object_or_404(Book, ISBN=ISBN)
    reviews = Review.objects.filter(book=book)
    bookinstance = BookInstance.objects.filter(book=book)
    bookinstance_details = get_object_or_404(BookInstance, id=ISBN)
    
    context = {
        'details': details, 
        'book': book,
        'bookAvailability': bookinstance_details,
        'reviews': reviews
    }
    return render(request, "book.html", context)


# Account Views
def accountRegister(request): 
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            id_num = request.POST["id_num"]
            security_question = request.POST["security_question"]
            security_answer = request.POST["security_answer"]
            username = request.POST["username"]
            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                id_num = id_num,
                security_question = security_question,
                role = 'regular',
                security_answer = security_answer,
                username = username,
            )
            user.set_password(request.POST["password"])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form':form})

def accountLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email       = request.POST["email"]
            password    = request.POST["password"]
            user        = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('library-home')
    else:
        form = LoginForm()
    return render(request, "login.html", {'form':form})

def accountProfile(request):
    context = {'user': request.user}
    return render(request, 'profile.html', context)

def accountLogout(request):
    logout(request)
    return redirect('library-home')

def accountChangePassword(request):
    user = User.objects.filter(first_name = request.user.first_name)
    details = get_object_or_404(User, first_name = request.user.first_name)
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            security_answer = request.POST["security_answer"]
            if security_answer == request.user.security_answer:
                details.set_password(request.POST["new_password"])
                details.save()
                updated_user = authenticate(request, email=request.user.email, password=request.POST["new_password"])
                login(request, updated_user)
                return redirect('library-home')
    else:
        form = PasswordChangeForm()
    return render(request, 'changePassword.html', {'form': form})

#we need a book view
#def book_detail(request, id, slug):
#    book = get_object_or_404(Book, id=id, slug=slug)
#    reviews = Review.objects.filter(book=book).order_by('-id')
#    
#    context = {
#        'book': book,
#       'reviews': reviews,
#    }
#    return render(request, 'library/book_detail')