# Proyecto Final Django: Blog Funcional y Autenticacion

Este es el repositorio de mi proyecto final de Desarrollo Web con Django. Es una plataforma de blog operativa que cumple con todos los requisitos pedidos en la consigna.

Autor: Candela Belluomini
Tecnologias: Python, Django, SQLite3, Git, GitHub.

---

## Descripcion del Proyecto

El proyecto consiste en un blog tipo plataforma web funcional, desarrollado en Python con el framework Django y base de datos SQLite3. Cuenta con un sistema seguro de registro e inicio de sesion de usuarios, manejo de perfiles editables, paginas dinamicas para la lectura de posts y paginas estaticas ("Acerca de mi" y "Contacto"). El superusuario dispone de control total mediante el panel de administracion nativo.

---

## Como ejecutar el proyecto de forma local

1. Clonar el repositorio:
   git clone https://github.com/CandeBelluomini/mi_proyecto_django.git

2. Activar el entorno virtual:
   En Windows: venv\Scripts\activate

3. Correr las migraciones de la Base de Datos:
   python manage.py migrate

4. Iniciar el servidor de desarrollo:
   python manage.py runserver

---

## URL Publica para Acceso

* Repositorio en GitHub: https://github.com/CandeBelluomini/mi_proyecto_django
* Nota sobre el Despliegue: El proyecto se encuentra estructurado y configurado en "Production Ready" mediante el archivo `requirements.txt` y los permisos de `ALLOWED_HOSTS` en `settings.py` para ser desplegado en servicios Cloud como Render o PythonAnywhere.

---

## Capturas de Pantalla (Evidencia de Funcionalidades)

Para demostrar el correcto funcionamiento de los criterios de aceptacion, se adjuntan las capturas de la aplicacion:

### 1. Panel de Administracion (Django Admin)
![Panel Admin](aca_va_el_link_de_tu_foto_del_admin)

### 2. Registro e Inicio de Sesion (Autenticacion)
![Login de Usuarios](aca_va_el_link_de_tu_foto_del_login)

### 3. Interfaz del Blog y Paginas Publicas
![Feed del Blog](aca_va_el_link_de_tu_foto_del_blog)

### 4. Perfil de Usuario Editable
![Perfil de Usuario](aca_va_el_link_de_tu_foto_del_perfil)