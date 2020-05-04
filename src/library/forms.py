from django import forms
from .models import User, Review, Book
from django.core.validators import RegexValidator

class RegisterForm(forms.ModelForm):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    password           = forms.CharField(min_length=6,widget=forms.PasswordInput, validators=[alphanumeric])
    id_num             = forms.IntegerField(label="I.D. Number")
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password", "id_num", "security_question", "security_answer"]
        widget = {'role': forms.HiddenInput()}

    def clean(self, *args, **kwargs):
        cleaned_data = self.cleaned_data
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        userInQuestion = User.objects.filter(username=username)
        emailInQuestion = User.objects.filter(email=email)
        if userInQuestion.exists():
            raise forms.ValidationError("Username is already taken")
        if emailInQuestion.exists():
            raise forms.ValidationError("Email is already in use")
        else:
            return cleaned_data

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
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)