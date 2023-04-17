from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from models import Aseguradora
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
import json


class AseguradoraView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        Aseguradoras = list(Aseguradora.objects.values())
        if (len(Aseguradoras)>0):
            datos = {'message':"Success", 'Aseguradoras': Aseguradoras}
        else:
            datos = {'message': "Aseguradoras no encontrados"}
        return JsonResponse(datos)
    
    def post(self, request):
        RequestBody = json.loads(request.body)
        Aseguradora.objects.create(
            Aseguradora = RequestBody['Aseguradora'],
            )
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put (self, request, id):
        RequestBody = json.loads(request.body)
        Aseguradoras = list(Aseguradora.objects.filter(id=id).values())
        if len(Aseguradoras) > 0:
            Aseguradoras = Aseguradora.objects.get(id=id)
            Aseguradoras.Aseguradora = RequestBody['Aseguradora']
            Aseguradoras.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Tipos de Pólizas no encontrados"}
        return JsonResponse(datos)
    
    def delete (self, id):
        Aseguradoras = list(Aseguradora.objects.filter(id=id).values())
        if len(Aseguradoras) > 0:
            Aseguradora.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Tipos de Pólizas no encontrados"}
        return JsonResponse(datos)
    