from django import forms
from .models import register

class registrationForm(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    password = forms.CharField()
    confirm_password = forms.CharField()
    # securityChoices = (
    #     ('In what city did you have your first ever birthday party?', 'In what city did you have your first ever birthday party?'),
    #     ('What is the last name of your Science class teacher in high school', 'What is the last name of your Science class teacher in high school'),
    #     ('Which company manufactured your first mobile phone?', 'Which company manufactured your first mobile phone?'),
    #     ('Who was your childhood hero?', 'Who was your childhood hero?'),
    #     ('Where was your best family vacation?', 'Where was your best family vacation?')
    # )
    # securityQuestion = forms.ChoiceField(choices = securityChoices)
    # securityAnswer = forms.CharField()

class registerForm(forms.ModelForm):
    class Meta: 
        model = register
        fields = ('firstName','lastName','username','email','password','confirm_password')

