from django.shortcuts import render
from django.http import HttpRequest
from .models import Citacoes


def index(request):
    citacoes = Citacoes.objects.all()
    return render(request,'index.html', {'citacoes':citacoes})
