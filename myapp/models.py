from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.CharField(max_length=255, null=False, blank=False)
    whatsapp = models.TextField(max_length=12)
    cnpj = models.TextField(max_length=12)
    desc = models.TextField(max_length=255)
