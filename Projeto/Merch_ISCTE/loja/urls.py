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

    # ex: loja/loginpage
    path('loginpage', views.loginpage, name='loginpage'),

    # ex: loja/perfil
    path('perfil', views.perfil, name='perfil'),

    # ex: loja/adicionar_carrinho
    path('adicionar_carrinho', views.adicionar_carrinho, name='adicionar_carrinho'),
    # ex: loja/carrinho
    path('carrinho', views.carrinho, name='carrinho'),

]
