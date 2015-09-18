from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from .models import Entrada


# Create your views here.

def index(request):
    entradas = Entrada.objects.all()
    return render(request, 'Entrada/index.html')