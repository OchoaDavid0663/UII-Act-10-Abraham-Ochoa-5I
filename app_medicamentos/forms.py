from django import forms
from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['id_proveedor', 'nombre', 'funcion', 'presentacion', 'precio', 'stock', 'f_caducidad']
        labels = {
            'id_proveedor' : 'Id_proveedor',
            'nombre' : 'Nombre',
            'funcion' : 'Funcion',
            'presentacion' : 'Presentacion',
            'precio' : 'Precio',
            'stock' : 'Stock',
            'f_caducidad' : 'F_caducidad'
        }

        widgets = {
            'id_proveedor' : forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'funcion' : forms.TextInput(attrs={'class': 'form-control'}),
            'presentacion' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.NumberInput(attrs={'class': 'form-control'}),
            'stock' : forms.NumberInput(attrs={'class': 'form-control'}),
            'f_caducidad' : forms.DateInput(attrs={'class': 'form-control'})
        }