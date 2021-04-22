from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)#Conectaos esta fila a la tabla Usuarios de los modelos por defecto de django
	imagenes = models.ImageField(default='foto_perfil.png')
	def __str__(self):
		return f'Perfil de {self.user.username}' #definimos una cadena de caracteres para poder ser mas visual en el admin de django

	def following(self):
		user_ids = Relationship.objects.filter(from_user=self.user).values_list('to_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)

	def followers(self):
		user_ids = Relationship.objects.filter(to_user=self.user).values_list('from_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') #con el related name asociamos todos los posts que tiene un usuario, por asi decirlo es como añadir una fila post a la tabla de usuarios
	timestamp = models.DateTimeField(default=timezone.now) #fecha de creacion del post
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp'] #Clase meta sirve para saber como se comporta la clase Post, con esto ordenamos Post, el - sirve àra que se cree en orden ascendente

	def __str__(self):
		return f'{self.user.username}: {self.content}' # aqui identificamos el usuario y el post que hizo el usuario , para facilitar el visionado de la tabla

class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'

	class Meta:
		indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		]

