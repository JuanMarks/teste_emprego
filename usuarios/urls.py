from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('cadastro_empresa', views.cadastro_empresa, name='cadastro_empresa'),
    path('dashboard_empresa', views.dashboard_empresa, name='dashboard_empresa'),
    path('logout', views.logout, name='logout'),
    path('apagar/<int:id>', views.apagar_vaga, name='apagar-vaga'),
    path('editar/<int:id>', views.editar_vaga, name='editar-vaga'),
    path('saibamais/<int:id>', views.saibamais, name='saibamais'),
    path('cadastro_inscricao/<int:id>', views.cadastro_inscricao, name='cadastro-inscricao'),
    
]