from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    preco_produto = models.FloatField()
    marca_produto = models.CharField(max_length=100)
    # reviewScore = #
    favorito = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_produto
