from django.forms import ModelForm
from .models import Cliente
from django import forms


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
        }
