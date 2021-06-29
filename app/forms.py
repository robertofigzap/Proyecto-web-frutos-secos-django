from django import forms
from django.db.models import fields
from .models import Despacho, Producto

class DespachoForm(forms.ModelForm):
    class Meta:
        model = Despacho
        fields = '__all__'
