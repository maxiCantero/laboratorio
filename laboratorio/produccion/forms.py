from django import forms
from .models import Equipo, Linea
from django.forms import BaseInlineFormSet
from django.forms import inlineformset_factory

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['tipodeEquipo','numero_de_serie','estado','imei','linea'] 
        estado = forms.CharField(max_length=100)
        tipodeEquipo = forms.CharField(max_length=100)
        numero_de_serie = forms.CharField(max_length=10)
        imei = forms.CharField(max_length=20)
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['linea'].queryset = Linea.objects.filter(estado='Stock')
        
class BaseEquipoFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        queryset = kwargs.pop('queryset', Linea.objects.filter(estado='Stock'))
        super().__init__(*args, **kwargs)
        self.queryset = queryset


class LineaForm(forms.ModelForm):
    class Meta:
        model = Linea
        fields = ['numero_de_telefono','numero_de_serie','estado','empresa','plan']
       