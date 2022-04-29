from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from six import string_types


class Produto(models.Model):
    produto_nome = models.CharField(max_length=50)
    produto_texto = models.CharField(max_length=200)
    preco_data = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    pub_data = models.DateTimeField('data de publicacao')
    foto = models.CharField(max_length=100, default='/loja/static/media/avatardefault.png')

    def __str__(self):
        return self.produto_nome

    def foi_publicada_recentemente(self):
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1)


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    curso = models.CharField(max_length=100)
    foto = models.CharField(max_length=100, default='/votacao/static/media/avatardefault.png')


class Conta(models.Model):
    info = models.OneToOneField(User, on_delete=models.CASCADE)


