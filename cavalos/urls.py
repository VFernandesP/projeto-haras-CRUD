from django.urls import path
from . import views

app_name = 'cavalos'
urlpatterns = [
    path('', views.lista_cavalos, name='lista_cavalos'),
    path('<int:pk>/', views.detalhe_cavalo, name='detalhe_cavalo'),
    path('criar/', views.criar_cavalo, name='criar_cavalo'),
    path('<int:pk>/editar/', views.editar_cavalo, name='editar_cavalo'),
    path('<int:pk>/excluir/', views.excluir_cavalo, name='excluir_cavalo'),
]    