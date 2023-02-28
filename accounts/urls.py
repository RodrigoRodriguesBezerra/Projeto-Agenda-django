from django.urls import path
from . import views

urlpatterns = [
    path('', views.entrar, name='index_entrar'),
    path('login/', views.entrar, name='entrar'),
    path('logout/', views.sair, name='sair'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard', views.dashboard, name='dashboard'),
]
