
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .utils import encrypt_data

@login_required
def crypto_demo_view(request):
    sample = "Sensitive transaction data"
    encrypted = encrypt_data(sample)
    return render(request, "security/demo.html", {
        "sample": sample,
        "encrypted": encrypted,
    })
