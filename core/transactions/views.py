
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TransactionForm
from .models import Transaction

@login_required
def create_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            Transaction.objects.create(
                user=request.user,
                amount=form.cleaned_data["amount"],
                merchant=form.cleaned_data["merchant"]
            )
            return redirect("transaction_list")
    else:
        form = TransactionForm()
    return render(request, "transactions/create.html", {"form": form})

@login_required
def list_transactions(request):
    tx = Transaction.objects.filter(user=request.user)
    return render(request, "transactions/list.html", {"transactions": tx})
