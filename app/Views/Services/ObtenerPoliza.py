from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from ...models import Poliza, Tipo_Poliza, Estado_Poliza
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import models
import datetime

#Obtener la lista de pólizas del tipo GASTOS MÉDICOS, con estado
#VENCIDA, con fecha de vigencia menores al 15/Febrero/2021.

class ObtenerPoliza (View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def ObtenerPolizas(self, request):
        ParametroTipoPoliza = 'Gastos Médicos'
        ParametroEstadoPoliza = 'Vencida'
        ParametroVigencia = datetime.date(2021, 2, 15)
        GetPolizas = list(Poliza.objects.filter(
            Tipo_Poliza = ParametroTipoPoliza,
            Estado_Poliza = ParametroEstadoPoliza,
            Fecha_Vigencia = ParametroVigencia
            ).values())
        if (len(GetPolizas)>0):
            datos = {'message':"Se han encontrado las polizas solicitadas", 'Polizas': GetPolizas}
        else:
            datos = {'message': "Polizas no encontrados"}
        return JsonResponse(datos)