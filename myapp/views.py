from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #salvar os dados da tela
    novo_usuario = Usuario()
    novo_usuario.empresa = request.POST.get('empresa')
    novo_usuario.CNPJ = request.POST.get('CNPJ')
    novo_usuario.save()

#exibir os dados salvos
    usuarios = {
        'usuarios': Usuario.objects.all()
        }

    return render(request, 'usuarios/usuarios.html', usuarios)