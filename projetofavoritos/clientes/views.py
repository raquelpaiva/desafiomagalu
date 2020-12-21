from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente
# Create your views here.

@login_required
def index(request):
  #  cliente = Cliente.objects.all()
    #return render(request, 'cadastro_cliente.html', {cliente: cliente}) #
   return render (request, 'index.html')

@login_required
def novo_cliente(request):   
    form = ClienteForm(request.POST or None, request.FILES or None)
   
    if form.is_valid():
        form.save()
        return redirect('/clientes/listarcliente')
    
    return render(request, 'novo_cliente_form.html', {'form': form}) 

@login_required
def atualizar_cliente(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = cadastro_cliente(request.POST or None, request.FILES or None, instance = pessoa)

    if form.is_valid():
        form.save()
        return redirect('cadastrocliente')
 
    return render(request, 'novo_cliente_form.html',{'form': form})
    
@login_required
def deletar_cliente(request,id):
    pessoa = ge_object_or_404(Pessoa, pk=id)
    form = cadastro_cliente(request.POST or None, request.FILES or None, instance = pessoa)

    if request.method == 'POST':
        pessoa.deletar()
        return redirect('cadastrocliente')
 
    return render(request, 'confirmacao_cad_deletado', {'pessoa: pessoa'})
    
@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('nome') 
    return render(request,'lista_clientes.html',{'clientes': clientes})
    
