from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Empresa, Linea, Plan, Equipo, TipoDeEquipo

admin.site.register(Empresa)
admin.site.register(Linea)
admin.site.register(Plan)
admin.site.register(Equipo)
admin.site.register(TipoDeEquipo)