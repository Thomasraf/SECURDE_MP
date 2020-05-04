from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import Account, Book
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.hashers import make_password


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
            hashed_password = make_password(request.POST["password"])
            Account.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                id_num = id_num,
                security_question = security_question,
                security_answer = security_answer,
                username = username, 
                password = hashed_password
            )
            account = authenticate(request, username=username, password=hashed_password, backend='django.contrib.auth.backends.ModelBackend')
            print(account)
            login(request, account)
            return redirect('library-home')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form':form})

def accountLogin(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = request.POST["username"]
        password = request.POST['password']
        account = authenticate(username=username, password=password)
        login(request, user)
        return redirect('library-home')
    else:
        form = LoginForm()
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
