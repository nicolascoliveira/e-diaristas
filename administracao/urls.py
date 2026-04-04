from django.urls import path
from .views import servico_views, usuario_views

urlpatterns = [
    path('servicos/cadastrar', servico_views.cadastrar_servico, name='cadastrar_servico'),
    path('servicos/listar', servico_views.listar_servicos, name='listar_servicos'),
    path('servicos/editar/<int:id>', servico_views.editar_servico, name='editar_servico'),
    path('servicos/excluir/<int:id>', servico_views.excluir_servico, name='excluir_servico'),
    path('usuarios/cadastrar/', usuario_views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/listar/', usuario_views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/editar/<int:id>', usuario_views.editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:id>', usuario_views.excluir_usuario, name='excluir_usuario'),
]
