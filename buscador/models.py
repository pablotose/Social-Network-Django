from django.db import models
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
# Create your models here.

class ExampleModel(DjangoCassandraModel):
	example_id = columns.UUID(primary_key=True, default=uuid.uuid4)
	#example_type = columns.Integer(index=True)
	#created_at = columns.DateTime()
	description = columns.Text(required=False)