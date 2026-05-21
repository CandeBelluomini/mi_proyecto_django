from django.urls import path
from productos.views import listado, crear_maquillaje, detalle_maquillaje, BorrarMaquillaje, ActualizarMaquillaje

app_name = "productos"

urlpatterns = [
    path("", listado, name="listado_maquillaje"),
    path("crear/", crear_maquillaje, name="crear_maquillaje"),
    path("<clave_primaria>/", detalle_maquillaje, name="detalle_maquillaje"),
    path("<pk>/borrar/", BorrarMaquillaje.as_view(), name="borrar_maquillaje"),
    path("<pk>/actualizar/", ActualizarMaquillaje.as_view(), name="actualizar_maquillaje")
]
