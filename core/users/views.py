from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, PrivacyConsentForm
from .models import PrivacyConsent

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            PrivacyConsent.objects.create(user=user)  # default record
            messages.success(request, "Account created. Please log in.")
            return redirect("users:login")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )
            if user:
                login(request, user)
                return redirect("dashboard:home")
            messages.error(request, "Invalid credentials.")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    return redirect("users:login")

@login_required
def privacy_view(request):
    consent, _ = PrivacyConsent.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = PrivacyConsentForm(request.POST, instance=consent)
        if form.is_valid():
            form.save()
            messages.success(request, "Privacy preferences updated.")
            return redirect("dashboard:home")
    else:
        form = PrivacyConsentForm(instance=consent)
    return render(request, "users/privacy.html", {"form": form})
