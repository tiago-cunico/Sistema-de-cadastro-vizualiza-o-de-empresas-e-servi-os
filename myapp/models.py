from django.db import models
#campo de cadastro empresa, id de usuario, empresa,whatsapp,cnpj,descrição.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.CharField(max_length=255, null=False, blank=False)
    whatsapp = models.TextField(max_length=12)
    cnpj = models.TextField(max_length=12)
    desc = models.TextField(max_length=255)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)  # Campo de imagem    
