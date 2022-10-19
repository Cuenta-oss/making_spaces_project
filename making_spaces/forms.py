from email import message
from unicodedata import name
from django import forms
from .models import contactModel
# from .models import contactModel

class contactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class':'form-control', 'placeholder':'Nombre', 'name':'name'})    
        self.fields['correo'].widget.attrs.update({'class':'form-control', 'placeholder':'Correo', 'name':'email'})    
        self.fields['telefono'].widget.attrs.update({'class':'form-control', 'placeholder':'Teléfono', 'name':'phone'})    
        self.fields['mensaje'].widget.attrs.update({'class':'form-control', 'placeholder':'Mensaje', 'name':'message', 'rows':6})    
            
    class Meta:
        model = contactModel
        fields = ['nombre', 'correo', 'telefono', 'mensaje']