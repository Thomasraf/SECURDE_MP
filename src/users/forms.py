from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

QUESTION_CHOICES = [
    ('city', 'In what city did you have your first ever birthday party?'),
    ('science', 'What is the last name of your Science class teacher in high school?'),
    ('phone', 'Which company manufactured your first mobile phone?'),
    ('hero', 'Who was your childhood hero?'),
    ('vacation', 'Where was your best family vacation?'),
]

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstName           = forms.CharField(max_length=15)
    lastName            = forms.CharField(max_length=10)
    idNum               = forms.IntegerField(label="I.D. Number")
    securityQuestion    = forms.CharField(label="Choose A Security Question", widget=forms.Select(choices=QUESTION_CHOICES))
    securityAnswer      = forms.CharField(max_length=20, label="Security Answer")

    class Meta:
        model = User
        fields = ["firstName", "lastName", "username", "password1", "password2", "email", "idNum", "securityQuestion", "securityAnswer"]
