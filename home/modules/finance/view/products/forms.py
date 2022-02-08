from home.modules.finance.models import RoomProduct
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = RoomProduct
        fields = ('name', 'shop', 'cost', 'per_kg', 'category')