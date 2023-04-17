from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from models import Asegurado
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
import json


class AseguradoView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        Asegurados = list(Asegurado.objects.values())
        if (len(Asegurados)>0):
            datos = {'message':"Success", 'Asegurados': Asegurados}
        else:
            datos = {'message': "Asegurados no encontrados"}
        return JsonResponse(datos)
    
    def post(self, request):
        RequestBody = json.loads(request.body)
        Asegurado.objects.create(
            Nombre_Asegurado = RequestBody['Nombre_Asegurado'],
            Edad = RequestBody['Edad'],
            )
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put (self, request, id):
        RequestBody = json.loads(request.body)
        Asegurados = list(Asegurado.objects.filter(id=id).values())
        if len(Asegurados) > 0:
            Asegurados = Asegurado.objects.get(id=id)
            Asegurados.Nombre_Asegurado = RequestBody['Nombre_Asegurado']
            Asegurados.Edad = RequestBody['Edad']
            Asegurados.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Asegurado no encontrado"}
        return JsonResponse(datos)
    
    def delete (self, id):
        Asegurados = list(Asegurado.objects.filter(id=id).values())
        if len(Asegurados) > 0:
            Asegurado.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Asegurado no encontrado"}
        return JsonResponse(datos)
    