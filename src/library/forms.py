from django import forms
from .models import Account

class RegisterForm(forms.ModelForm):
    password           = forms.CharField(widget=forms.PasswordInput)
    id_num             = forms.IntegerField(label="I.D. Number")
    
    class Meta:
        model = Account
        fields = ["first_name", "last_name", "username", "email", "password", "id_num", "security_question", "security_answer"]
        widget = {'role': forms.HiddenInput()}

    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        userInQuestion = Account.objects.filter(username=username)
        emailInQuestion = Account.objects.filter(email=email)
        if userInQuestion.exists():
            raise forms.ValidationError("Username is already taken")
        if emailInQuestion.exists():
            raise forms.ValidationError("Email is already in use")
        return username

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= Account
        fields = ["username", "password"]

        def clean(self, *args, **kwargs):
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')

            if username and password:
                user = authenticate(username=username, password=password)
                if not user:
                    raise forms.ValidationError('This user does not exist')
                if not user.check_password(password):
                    raise forms.ValidationError('Incorrect Password')
            return username