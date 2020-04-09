from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registrationForm, registerForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            print(username, email)

    form = registrationForm()
    return render(request, 'users/register.html', {'form': form})
    

def register_detail(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            print('VALID')

    form = registerForm()
    return render(request, 'users/register.html', {'form': form})