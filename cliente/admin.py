from django.contrib import admin
from .models import Cliente, TipoCliente, Departamento, Municipio, Direccion

# Register your models here.
admin.site.register(Cliente)
admin.site.register(TipoCliente)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Direccion)  
