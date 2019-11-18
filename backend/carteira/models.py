from django.db import models
from django_mongoengine import Document, EmbeddedDocument, fields

# Create your models here.

class Atual(Document):

    stock = fields.StringField( max_length=255)
    open = fields.DecimalField(max_digits=10, decimal_places=2)
    high = fields.DecimalField(max_digits=10, decimal_places=2)
    low = fields.DecimalField(max_digits=10, decimal_places=2)
    close = fields.DecimalField(max_digits=10, decimal_places=2)
    volume = fields.DecimalField(max_digits=10, decimal_places=2)
    date = fields.StringField(max_length=60)

class Ativos(Document):
    Company = fields.StringField( max_length=255)
    Stock = fields.StringField(max_length=60)


class Historico(Document):
    stock = fields.StringField( max_length=255)
    open = fields.DecimalField(max_digits=10, decimal_places=2)
    high = fields.DecimalField(max_digits=10, decimal_places=2)
    low = fields.DecimalField(max_digits=10, decimal_places=2)
    close = fields.DecimalField(max_digits=10, decimal_places=2)
    volume = fields.DecimalField(max_digits=10, decimal_places=2)
    date = fields.StringField(max_length=60)