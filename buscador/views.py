from django.shortcuts import render
import requests
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
#from django.shortcuts import render_to_response
from .models import Usuarios_buscador
from cassandra.cluster import Cluster

# Create your views here.

cluster = Cluster(['127.0.0.1'])


def lista_usuarios(request):
	q = request.GET.get('q', '')
	usuario = Usuarios_buscador.objects.filter(username=q)
	contexto = {'usuario': usuario}
	return render(request, 'buscador/buscador.html', contexto)


