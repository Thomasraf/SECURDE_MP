from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import Account
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.hashers import make_password

# Create your views here.

def accountRegister(request): 
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # if form.is_valid():
        #     account = form.save()
        #     account.first_name = form.cleaned_data.get('first_name')
        #     account.last_name = form.cleaned_data.get('last_name')
        #     account.email = form.cleaned_data.get('email')
        #     account.id_num = form.cleaned_data.get('id_num')
        #     account.security_question = form.cleaned_data.get('security_question')
        #     account.security_answer = form.cleaned_data.get('security_answer')
        #     account.save()
        #     username = form.cleaned_data.get('username')
        #     password = form.cleaned_data.get('password')
        #     hashed_password = make_password(password)
        #     user = authenticate(request, username=username, password=hashed_password)
        #     print(user)
        #     print(username)
        #     print(password)
        #     print(hashed_password)
        #     login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        #     return redirect('library-home')
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
            user = authenticate(request, username=username, password=hashed_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('library-home')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form':form})

def accountLogin(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
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