from django.db import models


class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    preco_produto = models.FloatField()
    marca_produto = models.CharField(max_length=100)
    reviewScore = models.SmallIntegerField()
    favorito = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_produto
