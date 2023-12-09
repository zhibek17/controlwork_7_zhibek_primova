from django import forms
from .models import GuestBook


class GuestForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ['name', 'email', 'text']
