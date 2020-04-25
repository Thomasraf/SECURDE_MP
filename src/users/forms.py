from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
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
    email               = forms.EmailField(label='Email Address')
    first_name           = forms.CharField(max_length=15, label='First Name')
    last_name            = forms.CharField(max_length=10, label='Last Name')
    password1           = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2           = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    id_num               = forms.IntegerField(label="I.D. Number")
    security_question    = forms.CharField(label="Choose A Security Question", widget=forms.Select(choices=QUESTION_CHOICES))
    security_answer      = forms.CharField(max_length=20, label="Security Answer")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2", "id_num", "security_question", "security_answer"]

    def clean_data(self, *args, **kwargs):
        username_qs = User.objects.filter(username=username)
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if username_qs.exists():
            raise forms.ValidationError("This account has already been registered")
        if password1 != password1:
            raise forms.ValidationError("Password do not match")
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password1')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
            if not user.is_active:
                raise forms.ValidationError('This User Is Not Active')
        return super(LoginForm, self).clean(*args, **kwargs)
