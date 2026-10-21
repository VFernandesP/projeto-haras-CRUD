from django.urls import path
from . import views

app_name = 'cavalos'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('cavalos/', views.lista_cavalos, name='lista_cavalos'),
    path('cavalos/criar/', views.criar_cavalo, name='criar_cavalo'),
    path('cavalos/<int:pk>/', views.detalhe_cavalo, name='detalhe_cavalo'),
    path('cavalos/<int:pk>/editar/', views.editar_cavalo, name='editar_cavalo'),
    path('cavalos/<int:pk>/excluir/', views.excluir_cavalo, name='excluir_cavalo'),
]