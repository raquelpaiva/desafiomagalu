from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente


def index(request):
   return render(request, 'clientes.html')

def novo_cliente(request):
    form = ClienteForm(request.POST or None, request.FILES or None)
   
    if form.is_valid():
        form.save()
        return redirect('/clientes/listarcliente')

    return render(request, 'novo_cliente_form.html', {'form': form}) 


def atualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance = cliente)

    if form.is_valid():
        form.save()
        return redirect('/clientes/listarcliente')
 
    return render(request, 'novo_cliente_form.html', {'form': form}) 


def deletar_cliente(request,id):
    Cliente.objects.filter(id=id).delete()

    return redirect('/clientes/listarcliente')


def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('nome') 
    return render(request,'lista_clientes.html',{'clientes': clientes})
    
