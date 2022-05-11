from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    categoria_nome = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria_nome


class Produto(models.Model):
    produto_nome = models.CharField(max_length=50)
    produto_texto = models.CharField(max_length=200)
    preco_data = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    categoria = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.RESTRICT)
    # prevemos que apagar uma categoria significa uma alteração manual, e a reposição será manual também
    foto = models.CharField(max_length=100, default='/static/media/defaultProduct.png')

    def __str__(self):
        return self.produto_nome

    def get_preco(self):
        return self.preco_data

    def serialize(self):
        return self.__dict__


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    curso = models.CharField(max_length=100)
    foto = models.CharField(max_length=100, default='/static/media/avatardefault.png')
