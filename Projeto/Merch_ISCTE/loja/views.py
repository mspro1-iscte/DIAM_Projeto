from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from .models import Cliente, Produto


def index(request):
    return render(request, 'loja/index.html')


@login_required(login_url='/loja/loginpage')
def detalhe(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'loja/detalhe.html', {'produto': produto})


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
    return render(request, 'loja/loginpage.html')


def perfil(request):
    cliente = Cliente.objects.filter(user=request.user)
    return render(request, 'loja/perfil.html', {'cliente': cliente})


def loginview(request):
    username = request.POST['username']
    password = request.POST['pass']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('loja:index'))
    else:
        return render(request, 'loja/loginpage.html')


def loginpage(request):
    return render(request, 'loja/loginpage.html')


def logoutview(request):
    logout(request)
    return render(request, 'loja/loginpage.html')


def registaruser(request):
    return render(request, 'loja/registaruser.html')
