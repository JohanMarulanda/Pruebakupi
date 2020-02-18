from django import forms
from .models import cliente, ciudad, departamento

class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['cedula', 'nombre', 'telefono', 'correo', 'ciudad']


class ciudadForm(forms.ModelForm):
    class Meta:
        model = ciudad
        fields = ['idCiudad', 'nomCiudad', 'idDepartamento']


class departamentoForm(forms.ModelForm):
    class Meta:
        model = departamento
        fields = ['idDepartamento', 'nomDepartamento']
