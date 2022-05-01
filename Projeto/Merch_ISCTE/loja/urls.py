from django.urls import include, path
from . import views

app_name = 'loja'
urlpatterns = [
    # ex: loja/
    path("", views.index, name="index"),

    # ex: loja/registaruser
    path('registaruser', views.registaruser, name='registaruser'),
    # ex: loja/registo
    path('registo', views.registo, name='registo'),

    # ex: loja/loginview
    path('loginview', views.loginview, name='loginview'),
    # ex: loja/logoutview
    path('logoutview', views.logoutview, name='logoutview'),


    # ex: loja/perfil
    path('perfil', views.perfil, name='perfil'),

    # ex: loja/adicionar_carrinho
    path('adicionar_carrinho', views.adicionar_carrinho, name='adicionar_carrinho'),
    # ex: loja/carrinho
    path('carrinho', views.carrinho, name='carrinho'),

    # ex: loja/detalhe_produto
    path('detalhe_produto', views.detalhe_produto, name='detalhe_produto'),

    # ex: loja/detalhe_categoria
    path('detalhe_categoria', views.detalhe_categoria, name='detalhe_categoria'),
    # ex: loja/nova_categoria
    path('nova_categoria', views.nova_categoria, name='nova_categoria'),

    # ex: loja/novo_produto
    path('novo_produto', views.novo_produto, name='novo_produto'),

]
