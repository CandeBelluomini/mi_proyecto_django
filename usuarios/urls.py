from django.urls import path 
from usuarios.views import iniciar_sesion, registrarse, perfil, editar_perfil, CambiarContraseña
from django.contrib.auth.views import LogoutView

app_name = "usuarios"

urlpatterns = [
    path("iniciar-sesion/", iniciar_sesion, name="iniciar_sesion"),
    path("registrarse/", registrarse, name="registro"),
    path("perfil/", perfil, name="perfil"),
    path("perfil/editar", editar_perfil, name="editar_perfil"),
    path("perfil/editar/contraseña", CambiarContraseña.as_view(), name="cambiar_contraseña"),
    path("cerrar-sesion/", LogoutView.as_view(template_name="usuarios/cerrar_sesion.html"), name="cerrar_sesion")
    
]