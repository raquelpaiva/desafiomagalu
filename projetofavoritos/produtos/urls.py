from django.urls import path, include
from .views import index
from .views import atualizar_produto
from .views import deletar_produto
from .views import novo_produto
from .views import lista_produtos

urlpatterns = [
    path('', index),
    path('novo_produto/', novo_produto, name= 'novo_produto'),
    path('atualizarproduto/<int:id>/', atualizar_produto, name='atualizarproduto'),
    path('deletarproduto/<int:id>/', deletar_produto, name='deletarproduto'),
    path('listarprodutos/', lista_produtos, name='listarprodutos'),

]
 



