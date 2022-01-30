from django import forms
from .models import Debt, Repay

class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = ('debtor', 'amount', 'description')


class RepayForm(forms.ModelForm):
    class Meta:
        model = Repay
        fields = ('debt', 'amount', 'description')