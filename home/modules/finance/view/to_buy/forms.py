from home.modules.finance.models import ToBuy
from django import forms

class ToBuyForm(forms.ModelForm):
    class Meta:
        model = ToBuy
        fields = ('product', 'shop')