from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from .models import Cliente, Produto, Categoria


def index(request):
    lista_categoria = Categoria.objects.all()
    context = {'lista_categoria': lista_categoria}
    return render(request, 'loja/index.html', context)


def loginview(request):
    username = request.POST['username']
    password = request.POST['pass']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('loja:index'))
    else:
        return HttpResponseRedirect(reverse('loja:index'))


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('loja:index'))


def registaruser(request):
    return render(request, 'loja/registaruser.html')


def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'loja/detalhe_produto.html', {'produto': produto})


def detalhe_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    lista_produtos = []
    for p in Produto.objects.all():
        if p.categoria_id == categoria_id:
            lista_produtos.append(p)
    context = {'lista_produtos': lista_produtos, 'categoria': categoria}
    return render(request, 'loja/detalhe_categoria.html', context)


def carrinho(request):
    return render(request, 'loja/carrinho.html')


def nova_categoria(request):
    categoria_nome = request.POST['categoria_nome']
    if bool(request.FILES.get('categoria_file', False)):
        myfile = request.FILES['categoria_file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        categoria = Categoria(categoria_nome=categoria_nome, foto=uploaded_file_url)
    else:
        categoria = Categoria(categoria_nome=categoria_nome)
    categoria.save()
    return HttpResponseRedirect(reverse('loja:index'))


def novo_produto(request):
    produto_nome = request.POST['produto_nome']
    produto_texto = request.POST['produto_texto']
    preco_data = request.POST['preco_data']
    categoria_select = request.POST['categoria_select']
    cat = get_object_or_404(Categoria, pk=categoria_select)

    if bool(request.FILES.get('produto_file', False)):
        myfile = request.FILES['produto_file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        produto = Produto(produto_nome=produto_nome, produto_texto=produto_texto, preco_data=preco_data,
                          categoria=cat, foto=uploaded_file_url)

    else:
        produto = Produto(produto_nome=produto_nome, produto_texto=produto_texto, preco_data=preco_data,
                          categoria=cat)
    produto.save()

    return HttpResponseRedirect(reverse('loja:index'))


def adicionar_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if 'lista_carrinho' not in request.session:
        request.session['lista_carrinho'] = [produto]

    else:
        lista_carrinho = request.session['lista_carrinho']
        lista_carrinho.append(produto)
        request.session['lista_carrinho'] = lista_carrinho
    return render(request, 'loja/detalhe_produto.html', {'produto': produto})


def remover_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if request.method == 'POST':
        remove_carrinho = request.POST['remove_carrinho']
        request.session['lista_carrinho'] -= [remove_carrinho]
    return render(request, 'loja/carrinho.html', {'produto': produto})


def registo(request):
    username = request.POST['username']
    password = request.POST['pass']
    email = request.POST.get('email')
    curso = request.POST['curso']
    user = User.objects.create_user(username, email, password)
    user.save()
    if bool(request.FILES.get('myfile', False)):
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        cliente = Cliente(user=user, curso=curso, foto=uploaded_file_url)
    else:
        cliente = Cliente(user=user, curso=curso)
    cliente.save()
    login(request, user)
    return HttpResponseRedirect(reverse('loja:index'))


def perfil(request):
    cliente = Cliente.objects.filter(user=request.user)
    return render(request, 'loja/perfil.html', {'cliente': cliente})


def apagar_categoria(request, categoria_id):
    record = Categoria.objects.get(id=categoria_id)
    record.delete()
    return HttpResponseRedirect(reverse('loja:index'))


def apagar_produto(request, produto_id):
    record = Produto.objects.get(id=produto_id)
    record.delete()
    return HttpResponseRedirect(reverse('loja:index'))

