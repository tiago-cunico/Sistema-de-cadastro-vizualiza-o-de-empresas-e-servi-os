
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('usuarios/', views.usuarios, name="listagem_usuarios"),
    path('usuarios/detalhes_usuario/<str:usuario_id>/', views.detalhes_usuario, name='detalhes_usuario'),
]
