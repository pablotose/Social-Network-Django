from django.shortcuts import render
import requests
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
#from django.shortcuts import render_to_response
from .models import Usuarios_buscador
from cassandra.cluster import Cluster

# Create your views here.

cluster = Cluster(['84.122.138.226'])


def lista_usuarios(request, username=None):
	q = request.GET.get('q', '')
	session = cluster.connect()
	session.set_keyspace("db")
	if q:
		usuario = session.execute("SELECT * from Usuarios_buscador where username like '{}%'".format(q))
		contexto = {'usuario': usuario}
		return render(request, 'buscador/buscador.html', contexto)
	else:
		usuario = session.execute("SELECT * from Usuarios_buscador")
		contexto = {'usuario': usuario}
		return render(request, 'buscador/buscador.html', contexto)


