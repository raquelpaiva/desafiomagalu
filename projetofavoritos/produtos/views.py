from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm
from .models import Produto
 

def index(request):
   return render(request, 'produtos.html')

def novo_produto(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)
   
    if form.is_valid():
        form.save()
        return redirect('/produtos/listarprodutos')

    return render(request, 'novo_produto_form.html', {'form': form}) 


def atualizar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance = produto)

    if form.is_valid():
        form.save()
        return redirect('/produtos/listarprodutos')
 
    return render(request, 'novo_produto_form.html', {'form': form}) 


def deletar_produto(request,id):
    Produto.objects.filter(id=id).delete()

    return redirect('/produtos/listarprodutos')


def lista_produtos(request):
    produtos = Produto.objects.all().order_by('nome_produto') 
    return render(request,'lista_produtos.html',{'produtos': produtos})
    
