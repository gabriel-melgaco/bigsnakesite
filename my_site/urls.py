
from django.contrib import admin
from django.urls import path
from core.views import login, cadastro, painel,contato

urlpatterns = [
    path('', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('painel/', painel, name='painel'),
    path('contato/', contato, name='contato'),
    path('admin/', admin.site.urls),
]
