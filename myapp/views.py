from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Usuario


def home(request):
    return render(request, 'usuarios/home.html')


# codigo da tela de cadastro de empresas 
def cadastro(request):
    return render(request, 'usuarios/cadastro.html')


def usuarios(request):
    
    #salvar os dados da tela
    novo_usuario = Usuario()
    novo_usuario.empresa = request.POST.get('empresa')
    novo_usuario.whatsapp = request.POST.get('whatsapp')
    novo_usuario.cnpj = request.POST.get('cnpj')
    novo_usuario.desc = request.POST.get('desc')



    if novo_usuario.empresa:
            novo_usuario.save()
    else:
            pass

#exibir os dados salvos
    usuarios = {
        'usuarios': Usuario.objects.all()
        }

    return render(request, 'usuarios/usuarios.html', usuarios)

def detalhes_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'usuarios/detalhes_usuario.html', {'usuario': usuario})
