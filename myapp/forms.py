import re

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import News

class ContactForm(forms.Form):
    subject = forms.CharField(label="Mavzu", widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    content = forms.CharField(label="Matn", widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}
    ))
    captcha = CaptchaField()

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Foydalanuvchi nomi", widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password = forms.CharField(label="Parol", widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Foydalanuvchi nomi", help_text=
    "Foydalanuvchi nomi 100 belgidan oshmasligi kerak", widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password1 = forms.CharField(label="Parol", widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Parolni tasdiqlash", widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label="e-mail", widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'slug', 'description', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError("Sarlavha raqam bilan boshlanmaydi")
        return title