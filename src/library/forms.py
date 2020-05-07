from django import forms
from .models import User, Review, Book
from django.core.validators import RegexValidator

class RegisterForm(forms.ModelForm):
    alphanumeric        = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    password           = forms.CharField(min_length=6,widget=forms.PasswordInput, validators=[alphanumeric])
    id_num             = forms.IntegerField(label="I.D. Number")
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "id_num", "security_question", "security_answer"]
        widget = {'role': forms.HiddenInput()}

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= User
        fields = ["username", "password"]

class AddBookForm(forms.ModelForm):
    year_of_pub =forms.CharField(label="Year Of Publication")
    dewey_call  =forms.CharField(label="Dewey Decimal System")
    
    class Meta:
        model = Book
        fields = ["title", "author", "publisher", "year_of_pub", "description", "ISBN", "dewey_call"]

class PasswordChangeForm(forms.ModelForm):
    alphanumeric            = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    new_password            = forms.CharField(min_length=6,widget=forms.PasswordInput, validators=[alphanumeric])
    
    class Meta:
        model = User
        fields = ["security_answer"]
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)