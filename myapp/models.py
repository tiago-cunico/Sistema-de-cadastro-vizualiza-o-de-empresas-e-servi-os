from django.db import models

class Usuario(models.Model):
    empresa = models.TextField(max_length=255)
    CNPJ = models.IntegerField()