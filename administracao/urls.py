from django.urls import path
from .views import auth_views, servico_views, usuario_views
from django.contrib.auth import views as django_auth_views

urlpatterns = [
    # Servicos
    path('servicos/cadastrar', servico_views.cadastrar_servico, name='cadastrar_servico'),
    path('servicos/listar', servico_views.listar_servicos, name='listar_servicos'),
    path('servicos/editar/<int:id>', servico_views.editar_servico, name='editar_servico'),
    path('servicos/excluir/<int:id>', servico_views.excluir_servico, name='excluir_servico'),
    
    # Usuarios
    path('usuarios/cadastrar', usuario_views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/listar', usuario_views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/editar/<int:id>', usuario_views.editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:id>', usuario_views.excluir_usuario, name='excluir_usuario'),

    # Autenticacao
    path('autenticacao/login', django_auth_views.LoginView.as_view(), name='logar_usuario'),
    path('autenticacao/logout', auth_views.LogoutGetView.as_view(), name='deslogar_usuario'),

]
