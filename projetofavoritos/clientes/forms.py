from django.forms import ModelForm
from .models import Novo_cliente 


class Novocliente_form(ModelForm):
     class Meta:
        model: Novo_cliente
        fields = ['nome', 'email']

class Cliente_form(ModelForm):
        nome = forms.CharField(max_length=200),
        email = forms.EmailField(max_length=100),