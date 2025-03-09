from django import forms
from .models import Usuario

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['empresa', 'whatsapp', 'cnpj', 'desc', 'logo']