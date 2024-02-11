from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')

def painel(request):
    return render(request, 'painel.html')


def contato(request):
    return render(request, 'contato.html')