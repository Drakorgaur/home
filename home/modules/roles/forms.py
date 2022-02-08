from django import forms
from .models import Role

class RoleForm(forms.ModelForm):

    class Meta:
        model = Role
        fields = ('role', 'user')



class FormUsernameBridge:
    def __init__(self, form, username):
        self.form = form
        self.username = username