
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('usuarios/', views.usuarios, name="listagem_usuarios"),
    path('usuarios/detalhes_usuario/<str:usuario_id>/', views.detalhes_usuario, name='detalhes_usuario'),
    path('cadastrar_empresa/', views.cadastrar_empresa, name='cadastrar_empresa'),
    path('upload_imagem/', views.upload_imagem, name='upload_imagem'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)