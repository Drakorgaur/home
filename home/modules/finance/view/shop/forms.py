from home.modules.finance.models import Shop
from django import forms

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('name', 'location')