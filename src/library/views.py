from django.shortcuts import render, redirect
from .models import Book
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 

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
    form = RegisterForm(request.POST)
    if form.is_valid():
        account = form.save()
        account.refresh_from_db()
        account.first_name = form.cleaned_data.get('first_name')
        account.last_name = form.cleaned_data.get('last_name')
        account.email = form.cleaned_data.get('email')
        account.id_num = form.cleaned_data.get('id_num')
        account.security_question = form.cleaned_data.get('security_question')
        account.security_answer = form.cleaned_data.get('security_answer')
        account.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('library-home')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form': form})

def accountLogin(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
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