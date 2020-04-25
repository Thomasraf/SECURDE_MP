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
    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.email = form.cleaned_data.get('email')
        user.id_num = form.cleaned_data.get('id_num')
        user.security_question = form.cleaned_data.get('security_question')
        user.security_answer = form.cleaned_data.get('security_answer')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('library-home')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form': form})

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
        return redirect('/home')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)

def userProfile(request):
    context = {'user': request.user}
    return render(request, 'profile.html', context)

def userLogout(request):
    auth.logout(request)
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