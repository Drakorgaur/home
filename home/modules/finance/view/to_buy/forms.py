from home.modules.finance.models import ToBuy, Shop
from django import forms

class ToBuyForm(forms.ModelForm):

    class Meta:
        model = ToBuy
        fields = ('shop',)


class ShopForm(forms.Form):
    objs = Shop.objects.all()
    choices = list()
    for obj in objs:
        choices.append((obj.pk, obj.name))
    shop = forms.CharField(
        widget=forms.Select(
            choices=choices
    ))