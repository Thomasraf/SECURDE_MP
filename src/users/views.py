from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def userRegister(request):
    next = request.GET.get('next')
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "register.html", context)

def userLogin(request):
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)

def userProfile(request):
    context = {'user': request.user}
    return render(request, 'profile.html', context)

def userLogout(request):
    logout(request)
    return redirect('/')

def userChangePassword(request):
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