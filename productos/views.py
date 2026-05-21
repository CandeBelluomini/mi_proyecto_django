from django.shortcuts import render, redirect
from productos.models import Maquillaje
from productos.forms import FormularioCreacionMaquillaje, FormularioCreacionMaquillajeCBV
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

def listado(request):
    
    productos = Maquillaje.objects.all()
    
    return render(request, "productos/listado.html", {"productos": productos})

def crear_maquillaje(request):
    
    print("POST: ", request.POST)
    print("GET: ", request.GET)
    
    if request.method =="POST":
        formulario = FormularioCreacionMaquillaje(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            maquillaje = Maquillaje(marca=data.get("marca"), descripcion=data.get("descripcion"), fecha=data.get("fecha"))
            maquillaje.save()
            return redirect("productos:listado_maquillaje")
    else:
        formulario = FormularioCreacionMaquillaje()
        
    return render(request, "productos/crear.html", {"formulario": formulario})

def detalle_maquillaje(request, clave_primaria):
    
    maquillaje = Maquillaje.objects.get(id=clave_primaria)
    
    return render(request, "productos/detalle.html", {"producto": maquillaje})

class BorrarMaquillaje(DeleteView):
    model = Maquillaje
    template_name = "productos/borrado.html"
    success_url = reverse_lazy("productos:listado_maquillaje")
    
class ActualizarMaquillaje(UpdateView):
    model = Maquillaje
    template_name = "productos/actualizar.html"
    success_url = reverse_lazy("productos:listado_maquillaje")
    #fields = ["marca", "descripcion"]
    #fields = ["marca", "descripcion", "fecha"]
    #fields = "__all__"
    form_class = FormularioCreacionMaquillajeCBV
    

