from django.forms import ModelForm
from .models import Produto
from django import forms


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
 