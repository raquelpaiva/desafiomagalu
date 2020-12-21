from django.shortcuts import render, redirect, get_object_or_404
from .models import Novo_cliente
from .forms import novo_cliente
# Create your views here.

def index(request):
    cliente = Cliente.objects.all()
    return render(request, 'cadastro_cliente.html', {cliente: cliente})


def novo_cliente(request):   
    form = novo_cliente_form(request.POST or None, request.FILES or None)
   
    if form.is_valid():
        form.save()
    return redirect("novocliente")
    return render(request, 'novo_cliente_form.html', {'form': form}) 

def atualizarcliente(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = cadastro_cliente(request.POST or None, request.FILES or None, instance = pessoa)

    if form.is_valid():
        form.save()
        return redirect('cadastrocliente')
 
    return render(request, 'novo_cliente_form.html',{'form': form})
    

def deletarcliente(request,id):
    pessoa = ge_object_or_404(Pessoa, pk=id)
    form = cadastro_cliente(request.POST or None, request.FILES or None, instance = pessoa)

    if request.method == 'POST':
        pessoa.deletar()
        return redirect('cadastrocliente')
 
    return render(request, 'confirmacao_cad_deletado', {'pessoa: pessoa'})
    
