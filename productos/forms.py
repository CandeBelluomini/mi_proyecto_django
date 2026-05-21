from django import forms
from productos.models import Maquillaje

class FormularioCreacionMaquillaje(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(widget=forms.Textarea)
    fecha = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    
    
class FormularioCreacionMaquillajeCBV(forms.ModelForm):
    #marca = forms.CharField(max_length=30)
    #descripcion = forms.CharField(widget=forms.Textarea)
    #fecha = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    
    
    class Meta:
        model = Maquillaje
        #fields = ["marca", "descripcion"]
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"})
        }

    
    
    