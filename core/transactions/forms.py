from django import forms

class TransactionForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    merchant = forms.CharField(max_length=120)
