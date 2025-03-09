from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Usuario
from django import forms
from .forms import EmpresaForm

def home(request):
    return render(request, 'usuarios/home.html')

#----------------------------------------------------------------------------------------------------------------------------

def detalhes_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'usuarios/detalhes_usuario.html', {'usuario': usuario})

#----------------------------------------------------------------------------------------------------------------------------

def usuarios(request):
    # Lógica para salvar os dados da tela (mantida do seu código original)
    novo_usuario = Usuario()
    novo_usuario.empresa = request.POST.get('empresa')
    novo_usuario.whatsapp = request.POST.get('whatsapp')
    novo_usuario.cnpj = request.POST.get('cnpj')
    novo_usuario.desc = request.POST.get('desc')

    if novo_usuario.empresa:
        novo_usuario.save()

    # Lógica de pesquisa
    termo_pesquisa = request.GET.get('q', '').strip()  # Pega o termo de pesquisa da URL
    usuarios_lista = Usuario.objects.all()

    if termo_pesquisa:
        usuarios_lista = usuarios_lista.filter(empresa__icontains=termo_pesquisa)  # Filtra pelo nome da empresa

    # Contexto para o template
    context = {
        'usuarios': usuarios_lista,
        'termo_pesquisa': termo_pesquisa,
    }

    return render(request, 'usuarios/usuarios.html', context)

#----------------------------------------------------------------------------------------------------------------------------

#codigo criação de um upload de imagem automatico abaixo
def cadastro(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listagem_usuarios')
    else:
        form = EmpresaForm()
    
    return render(request, 'usuarios/cadastro.html', {'form': form})

#----------------------------------------------------------------------------------------------------------------------------

def cadastrar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listagem_usuarios')
    else:
        form = EmpresaForm()
    
    return render(request, 'usuarios/cadastro.html', {'form': form})

#----------------------------------------------------------------------------------------------------------------------------

def upload_imagem(request):
    if request.method == 'POST':
        # Obtém a última empresa cadastrada (ou outra lógica para associar a imagem)
        empresa = Usuario.objects.latest('id')
        
        # Atualiza o campo 'logo' da empresa com a imagem enviada
        empresa.logo = request.FILES['logo']
        empresa.save()
        
        return redirect('listagem_usuarios')  # Redireciona para a listagem de usuários
    
    return render(request, 'cadastro.html')