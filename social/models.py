from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)#Conectaos esta fila a la tabla Usuarios de los modelos por defecto de django
	imagenes = models.ImageField(default='foto_perfil.png')
	def __str__(self):
		return f'Perfil de {self.user.username}' #definimos una cadena de caracteres para poder ser mas visual en el admin de django

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') #con el related name asociamos todos los posts que tiene un usuario, por asi decirlo es como añadir una fila post a la tabla de usuarios
	timestamp = models.DateTimeField(default=timezone.now) #fecha de creacion del post
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp'] #Clase meta sirve para saber como se comporta la clase Post, con esto ordenamos Post, el - sirve àra que se cree en orden ascendente

	def __str__(self):
		return f'{self.user.username}: {self.content}' # aqui identificamos el usuario y el post que hizo el usuario , para facilitar el visionado de la tabla
