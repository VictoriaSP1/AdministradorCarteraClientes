from django.contrib import admin
from .models import Agente, Asegurado, Cliente, Poliza, Estado_Poliza, Tipo_Poliza

admin.site.register(Agente)
admin.site.register(Asegurado)
admin.site.register(Cliente)
admin.site.register(Poliza)
admin.site.register(Estado_Poliza)
admin.site.register(Tipo_Poliza)
