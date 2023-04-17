from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from models import Poliza
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json


class PolizaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        Polizas = list(Poliza.objects.values())
        if (len(Polizas)>0):
            datos = {'message':"Success", 'Polizas': Polizas}
        else:
            datos = {'message': "Polizas no encontrados"}
        return JsonResponse(datos)
    
    def post(self, request):
        RequestBody = json.loads(request.body)
        Poliza.objects.create(
            Num_Poliza = RequestBody['Num_Poliza'],
            FechaInicio = RequestBody['FechaInicio'],
            FechaVigencia = RequestBody['FechaVigencia'],
            Id_Cliente = RequestBody['Id_Cliente'],
            Id_Asegurado = RequestBody['Id_Asegurado'],
            Id_Aseguradora = RequestBody['Id_Aseguradora'],
            Id_Tipo_Poliza = RequestBody['Id_Tipo_Poliza'],
            Precio = RequestBody['Precio'],
            Id_Estado_Poliza = RequestBody['Id_Estado_Poliza']
            )
        datos = {'message': "Se ha creado una poliza"}
        return JsonResponse(datos)
    
    def put (self, request, id):
        RequestBody = json.loads(request.body)
        Polizas = list(Poliza.objects.filter(id=id).values())
        if len(Polizas) > 0:
            Polizas = Poliza.objects.get(id=id)
            Polizas.Num_Poliza = RequestBody['Num_Poliza']
            Polizas.FechaInicio = RequestBody['FechaInicio']
            Polizas.FechaVigencia = RequestBody['FechaVigencia']
            Polizas.Id_Cliente = RequestBody['Id_Cliente']
            Polizas.Id_Asegurado = RequestBody['Id_Asegurado']
            Polizas.Id_Aseguradora = RequestBody['Id_Aseguradora']
            Polizas.Id_Tipo_Poliza = RequestBody['Id_Tipo_Poliza']
            Polizas.Precio = RequestBody['Precio']
            Polizas.Id_Estado_Poliza = RequestBody['Id_Estado_Poliza']
            Polizas.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Poliza no encontrada"}
        return JsonResponse(datos)
    
    def delete (self, id):
        Polizas = list(Poliza.objects.filter(id=id).values())
        if len(Polizas) > 0:
            Poliza.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Poliza no encontrada"}
        return JsonResponse(datos)
    