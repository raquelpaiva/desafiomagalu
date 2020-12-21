from django.urls import path, include
from . import views
from .views import atualizar_cliente
from .views import deletar_cliente
from .views import index
from .views import novo_cliente
from .views import lista_clientes

urlpatterns = [
    # Páginas usuário
    path('', index),
    path('novo_cliente/', novo_cliente, name= 'novo_cliente'),
    path('atualizarcliente/<int:id>/', atualizar_cliente, name='atualizarcliente'),
    path('deletarcliente/<int:id>/', deletar_cliente, name='deletarcliente'),
    path('listarcliente/', lista_clientes, name='listarclientes'),

]
 



