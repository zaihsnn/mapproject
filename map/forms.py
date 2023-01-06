from django.forms import ModelForm
from django import forms
from map.models import *

class FormTPI(ModelForm):
    class Meta:
        model = TPI
        fields = '__all__'

        widgets = {
            'nomer' : forms.NumberInput({'class':'form-control', 'required':'required'}),
            'nama' : forms.TextInput({'class':'form-control', 'placeholder':'nama', 'required':'required'}),
            'alamat' : forms.TextInput({'class':'form-control', 'placeholder':'alamat', 'required':'required'}),
            'jam_buka' : forms.TextInput({'class':'form-control', 'placeholder':'buka', 'required':'required'}),
            'gambar' : forms.TextInput({'class':'form-control', 'required':'required'}),
        }