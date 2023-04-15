from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from models import Tipo_Poliza
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
import json


class Tipo_PolizaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        Tipo_Polizas = list(Tipo_Poliza.objects.values())
        if (len(Tipo_Polizas)>0):
            datos = {'message':"Success", 'Tipo_Polizas': Tipo_Polizas}
        else:
            datos = {'message': "Tipo_Polizas no encontrados"}
        return JsonResponse(datos)
    
    def post(self, request):
        RequestBody = json.loads(request.body)
        Tipo_Poliza.objects.create(
            Tipo_Poliza = RequestBody['Tipo_Poliza'],
            )
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put (self, request, id):
        RequestBody = json.loads(request.body)
        Tipo_Polizas = list(Tipo_Poliza.objects.filter(id=id).values())
        if len(Tipo_Polizas) > 0:
            Tipo_Polizas = Tipo_Poliza.objects.get(id=id)
            Tipo_Polizas.Tipo_Poliza = RequestBody['Tipo_Poliza']
            Tipo_Polizas.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Tipos de Pólizas no encontrados"}
        return JsonResponse(datos)
    
    def delete (self, id):
        Tipo_Polizas = list(Tipo_Poliza.objects.filter(id=id).values())
        if len(Tipo_Polizas) > 0:
            Tipo_Poliza.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Tipos de Pólizas no encontrados"}
        return JsonResponse(datos)
    