from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import Q
User = get_user_model()


# Create your views here.
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
                imprint = BookInstance.objects.all().count() + 1,
                id = 1,
                ISBN = ISBN,
                status = 'a'
            )
            return redirect('library-home')
    else:
        form = AddBookForm()
    return render(request, "addBook.html", {'form': form})

def editBook(request, ISBN):
    book = Book.objects.get(ISBN=ISBN)
    form = EditBookForm(instance=book)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('library-home')
    return render(request, "editBook.html", {'form': form})

def addBookInstance(request, ISBN):
    if request.method == 'POST':
        form = AddBookInstanceForm(request.POST)
        if form.is_valid():
            imprint = request.POST["imprint"]
            BookInstance.objects.create(
                book = Book.objects.get(ISBN = ISBN),
                id = 1,
                ISBN = ISBN,
                status = 'a',
                imprint = imprint
            )
            return redirect('library-home')
    else:
        form = AddBookInstanceForm()
    return render(request, "addBookInstance.html", {'form': form})

def editBookInstance(request, ISBN):
    details = get_object_or_404(Book, ISBN=ISBN)
    bookInstance = BookInstance.objects.filter(ISBN=ISBN)
    context = {
        "bookInstance" : bookInstance,
        "details": details
    }
    return render(request, 'editBookInstance.html', context)

def editBookInstanceForm(request, imprint, ISBN):
    bookInstance = BookInstance.objects.get(imprint=imprint)
    form = EditBookInstanceForm(instance=bookInstance)
    if request.method == 'POST':
        form = EditBookInstanceForm(request.POST, instance=bookInstance)
        if form.is_valid():
            if request.POST["status"] == 'a':
                book = BookBorrow.objects.get(ISBN = ISBN)
                book.delete()
                form.save()
                return redirect('library-home')
            else:
                form.save()
                return redirect('library-home')
    return render(request, "editBookInstanceForm.html", {'form': form})

def deleteBookInstance(request, ISBN):
    details = get_object_or_404(Book, ISBN=ISBN)
    bookInstance = BookInstance.objects.filter(ISBN=ISBN)
    context = {
        "bookInstance": bookInstance,
        "details": details
    }
    return render(request, 'deleteBookInstance.html', context)

def deleteBookInstanceForm(request, imprint, ISBN):
    bookInstance = BookInstance.objects.get(imprint=imprint)
    if 'delete' in request.POST:
        bookInstance.delete()
        return redirect('library-home')
    if 'no' in request.POST:
        return redirect('library-home')
    return render(request, 'deleteBookInstanceForm.html')

def viewBook(request, ISBN):
    form = ReviewForm(request.POST)
    book = Book.objects.filter(ISBN=ISBN)
    details = get_object_or_404(Book, ISBN=ISBN)
    bookBorrow = BookBorrow.objects.filter(ISBN=ISBN)
    if 'review' in request.POST:
        content = request.POST["content"]
        Review.objects.create(
            title = details.title,
            userWhoCommented = request.user.username,
            content = content,
            timestamp = datetime.now(),
        )
        context = {
            'details': details, 
            'bookBorrow': bookBorrow,
            'reviews': Review.objects.filter(title=details.title),
            'user': request.user,
            'form': form
        }
        return HttpResponseRedirect(request.path_info)
        book = Book.objects.get(ISBN = ISBN)
        bookInstance = BookInstance.objects.filter(ISBN = ISBN)
        bookBorrow = BookBorrow.objects.filter(ISBN = ISBN)
        book.delete()
        bookInstance.delete()
        bookBorrow.delete()
        context = {
            'details': details, 
            'bookAvailability': bookinstance_details,
            'bookBorrow': bookBorrow,
            'bookInstances': bookInstances,
            'reviews': Review.objects.filter(title=details.title),
            'user': request.user,
            'form': form
        }
        return redirect('library-home')
    else:
        form = ReviewForm()
        context = {
            'details': details, 
            'bookBorrow': bookBorrow,
            'reviews': Review.objects.filter(title=details.title),
            'user': request.user,
            'form': form
        }
    return render(request, "book.html", context)

def bookInstance(request, ISBN):
    book = Book.objects.filter(ISBN=ISBN)
    details = get_object_or_404(Book, ISBN=ISBN)
    bookInstances = BookInstance.objects.filter(ISBN = ISBN)
    bookBorrow = BookBorrow.objects.filter(ISBN=ISBN)
    context = {
        'details': details,
        'bookBorrow': bookBorrow,
        'bookInstances': bookInstances,
        'reviews': Review.objects.filter(title=details.title),
        'user': request.user
    }
    return render(request, "bookInstance.html", context)

def bookInstanceManager(request, ISBN):
    book = Book.objects.filter(ISBN=ISBN)
    details = get_object_or_404(Book, ISBN=ISBN)
    bookBorrow = BookBorrow.objects.filter(ISBN=ISBN)

    if 'delete' in request.POST:
        book = Book.objects.get(ISBN = ISBN)
        bookInstance = BookInstance.objects.all()
        bookBorrow = BookBorrow.objects.all()
        book.delete()
        bookInstance.delete()
        bookBorrow.delete()
        context = {
            'details': details, 
            'bookBorrow': bookBorrow,
            'reviews': Review.objects.filter(title=details.title),
            'user': request.user
        }
        return redirect('library-home')
    else:
        context = {
            'details': details, 
            'bookBorrow': bookBorrow,
            'reviews': Review.objects.filter(title=details.title),
            'user': request.user
        }
    return render(request, "bookInstance.html", context)


def deleteBook(request, ISBN):
    details = get_object_or_404(Book, ISBN=ISBN)
    if 'delete' in request.POST:
        book = Book.objects.get(ISBN = ISBN)
        bookInstance = BookInstance.objects.all()
        bookBorrow = BookBorrow.objects.all()
        book.delete()
        bookInstance.delete()
        bookBorrow.delete()
        context = {
            'details': details, 
        }
        return redirect('library-home')
    if 'no' in request.POST:
        return redirect('library-home')
    else:
        context = {
            'details': details, 
        }
    return render(request, "deleteBook.html", context)

def borrowBookInstanceForm(request, imprint, ISBN):
    details = get_object_or_404(Book, ISBN=ISBN)
    bookInstance = BookInstance.objects.get(imprint=imprint)
    bookinstance_details = get_object_or_404(BookInstance, imprint=imprint)
    if 'borrow' in request.POST:
        BookBorrow.objects.create(
                title = details.title,
                author = details.author,
                publisher = details.publisher,
                year_of_pub = details.year_of_pub,
                description = details.description,
                ISBN = details.ISBN,
                dewey_call = details.dewey_call,
                userBorrowing = request.user.username,
                imprint = bookinstance_details.imprint,
            )
        bookinstance_details.status = 'r'
        bookinstance_details.save()
        context = {
            'details': details, 
            'bookAvailability': bookinstance_details,
            'bookInstance': bookInstance,
            'reviews': Review.objects.filter(title=details.title),
            'user': request.user
        }
        return redirect('library-home')
    if 'no' in request.POST:
        return redirect('library-home')
    context = {
            'details': details, 
            'bookAvailability': bookinstance_details,
            'bookInstance': bookInstance,
            'reviews': Review.objects.filter(title=details.title),
            'user': request.user
        }
    return render(request, "bookInstanceForm.html", context)


def returnBook(request, ISBN):
    returnBook = BookBorrow.objects.filter(userBorrowing = request.user.username)

    if 'yes' in request.POST:
        book = BookBorrow.objects.get(ISBN = ISBN)
        book.delete()
        bookInstance = BookInstance.objects.filter(ISBN = ISBN).update(status="a")
        context = {
            'user': request.user,
            'returnBook': returnBook
        }
        return render(request, 'profile.html', context)
    if 'no' in request.POST:
        context = {
            'user': request.user,
            'returnBook': returnBook
        }
        return render(request, 'profile.html', context)
    else:
        context = {
            'user': request.user,
            'returnBook': returnBook
        }
    return render(request, 'returnBook.html', context)


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

def managerRegister(request):
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
                role = 'manager',
                security_answer = security_answer,
                username = username,
            )
            user.set_password(request.POST["password"])
            user.save()
            return redirect('library-home')
    else:
        form = RegisterForm()
    return render(request, "registerManager.html", {'form':form})

def accountLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username       = request.POST["username"]
            password    = request.POST["password"]
            user        = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('library-home')
    else:
        form = LoginForm()
    return render(request, "login.html", {'form':form})

def accountProfile(request):
    borrowedBook = BookBorrow.objects.filter(userBorrowing = request.user.username)
    context = {
        'user': request.user,
        'borrowedBook': borrowedBook
        }
    return render(request, 'profile.html', context)


def accountLogout(request):
    logout(request)
    return redirect('library-home')

def accountChangePassword(request):
    user = User.objects.filter(first_name = request.user.username)
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

def accountForgotPassword(request):
    try:
        username = request.GET.get('username')
    except:
        username = None
    if username:
        user = User.objects.filter(username = username)
        context = {'query': username, 'user': user}
        template = 'changeForgottenPassword.html'
    else:
        template: 'forgotPassword.html'
        context = {}
    return render(request, 'forgotPassword.html', context)

def editForgottenPassword(request,username):
    form = ForgotPasswordChangeForm(request.POST)
    user = User.objects.filter(username=username)
    details = get_object_or_404(User, username = username)
    if request.METHOD == 'POST':
        form = ForgotPasswordChangeForm(request.POST)
        if form.is_valid():
            security_answer = request.POST["security_answer"]
            if security_answer == user.security_answer:
                details.set_password(request.POST["new_password"])
                details.save()
                updated_user = authenticate(request, email=user.email, password=request.POST["new_password"])
                login(request, updated_user)
                return redirect('library-home')

def error_400(request,exception):
    return render (request,'400.html')

def error_403(request,exception):
    return render (request,'403.html')

def error_404(request,exception):
    return render (request,'404.html')

def error_500(request):
    return render (request,'500.html')