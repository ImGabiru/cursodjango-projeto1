from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'global/home.html')


def contato(request):
    return HttpResponse('Me contate no zap: se vira pra descobrir o número')


def sobre(request):
    return HttpResponse('Eu sou eu!')
