from django.db import models
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
# Create your models here.

class Usuarios_buscador(DjangoCassandraModel):
	id_usuario = columns.UUID(primary_key=True, default=uuid.uuid4)
	username = columns.Text()
	email_address = columns.Text()

	def __str__(self):
		return f'Usuario : {self.username}'
