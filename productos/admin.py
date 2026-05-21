from django.contrib import admin
from productos.models import Maquillaje

#dmin.site.register(Maquillaje)

class MaquillajeAdmin(admin.ModelAdmin):
    list_display = ["marca", "descripcion"]
    search_fields = ["marca"]
    list_filter = ["fecha"]
    
admin.site.register(Maquillaje, MaquillajeAdmin)

