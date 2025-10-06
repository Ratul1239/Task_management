from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
import re
from django.contrib.auth.forms import AuthenticationForm
class register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2','email']
    
    def __init__(self, *args, **kwargs):
        super(register_form, self).__init__(*args, **kwargs)  # সঠিকভাবে parent class call
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None


class userregister_form(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))
    comfirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','password1','comfirm_password','email']
        widgets = {
            'username': forms.TextInput(attrs={'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'off'}),
        }
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This Username is already taken')
        return username
        
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This Email is already taken')
        return email
    def clean_password1(self):
        password1=self.cleaned_data.get('password1')
        errors=[]
        if len(password1)<8:
            errors.append('password must be at least 8 charater')
        if 'abc'not in password1:
            errors.append('password must inlude abc character')
        if errors:
            raise forms.ValidationError(errors)
        return password1
    

    def clean(self):
        cleaned_data=super().clean()
        password1=cleaned_data.get('password1')
        comfirm_password=cleaned_data.get('comfirm_password')
        if password1 !=comfirm_password:
            raise forms.ValidationError('password do not match')
        return cleaned_data
    
class MyAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # username এবং password input-এ attrs যোগ করছি
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'off',    # বা 'username'
            'autofocus': True,
            'placeholder': 'Username'
        })
        self.fields['password'].widget.attrs.update({
            'autocomplete': 'new-password',  # ব্যবহার করুন 'current-password' বা 'new-password' ব্রাউজার আচরণ অনুযায়ী
            'placeholder': 'Password'
        })
