from django.urls import path, include
from . import views
from .views import cliente
from .views import novo_cliente
from .views import atualizarcliente
from .views import deletarcliente

urlpatterns = [
    # Páginas usuário
    path('cliente/', cliente, name= 'cliente'),
    path('novo_cliente/', novo_cliente, name= 'novo_cliente'),
    path('atualizar/<init:id>/', atualizarcliente, name='atualizarcliente'),
    path('deletar/<init:id>/', deletarcliente, name='deletarcliente'),

]
 



