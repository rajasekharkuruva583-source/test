from django import forms
from django.contrib.auth.models import User
from .models import PrivacyConsent

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ["username", "email", "password"]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class PrivacyConsentForm(forms.ModelForm):
    class Meta:
        model = PrivacyConsent
        fields = ["consent_given", "data_sharing", "data_retention_days"]
