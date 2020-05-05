from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Book, Review
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
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


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'About'})

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
            Book.objects.create(
                title = title,
                author = author,
                publisher = publisher,
                year_of_pub = year_of_pub,
                description = description,
                ISBN = ISBN,
                dewey_call = dewey_call
            )
            return redirect('library-home')
    else:
        form = AddBookForm()
    return render(request, "addBook.html", {'form': form})

def viewBook(request, ISBN):
    book = Book.objects.filter(ISBN=ISBN)
    details = get_object_or_404(Book, ISBN=ISBN)
    reviews = Review.objects.filter(book=book)
    
    
    context = {
        'details': details, 
        'book': book,
        'reviews': reviews
    }
    return render(request, "book.html", context)

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
    form = LoginForm(request.POST)
    if form.is_valid():
        email = request.POST["email"]
        password = request.POST['password']
        user = authenticate(request,email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('library-home')
            print('worked')
        else:
            form = LoginForm()
            print('Did Not Work')
            print(email)
            print(password)
    return render(request, "login.html", {'form': form})

def accountProfile(request):
    context = {'user': request.user}
    return render(request, 'profile.html', context)

def accountLogout(request):
    logout(request)
    return redirect('library-home')

def accountChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/')
        
    else:
        form = PasswordChangeForm(user = request.user)
        context = {'form': form}
        return render(request, 'changePassword.html', context)

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