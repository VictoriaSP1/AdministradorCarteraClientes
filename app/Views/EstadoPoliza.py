from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from models import Estado_Poliza
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
import json


class Estado_PolizaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        Estado_Polizas = list(Estado_Poliza.objects.values())
        if (len(Estado_Polizas)>0):
            datos = {'message':"Success", 'Estado_Polizas': Estado_Polizas}
        else:
            datos = {'message': "Estados no encontrados"}
        return JsonResponse(datos)
    
    def post(self, request):
        RequestBody = json.loads(request.body)
        Estado_Poliza.objects.create(
            Estado_Poliza = RequestBody['Estado_Poliza'],
            )
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def PUT (self, request, id):
        RequestBody = json.loads(request.body)
        Estado_Polizas = list(Estado_Poliza.objects.filter(id=id).values())
        if len(Estado_Polizas) > 0:
            Estado_Polizas = Estado_Poliza.objects.get(id=id)
            Estado_Polizas.Estado_Poliza = RequestBody['Estado_Poliza']
            Estado_Polizas.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Estados de Póliza no encontrados"}
        return JsonResponse(datos)
    
    def delete (self, id):
        Estado_Polizas = list(Estado_Poliza.objects.filter(id=id).values())
        if len(Estado_Polizas) > 0:
            Estado_Poliza.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Estados de Póliza no encontrados"}
        return JsonResponse(datos)
    