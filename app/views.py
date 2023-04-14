from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from .models import Agente, Asegurado, Cliente, Poliza, Estado_Poliza, Tipo_Poliza
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
import json


class AgenteView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        Agentes = list(Agente.objects.values())
        if (len(Agentes)>0):
            datos = {'message':"Success", 'Agentes': Agentes}
        else:
            datos = {'message': "Agentes no encontrados"}
        return JsonResponse(datos)
    
    def post(self, request):
        RequestBody = json.loads(request.body)
        Agente.objects.create(
            Nombre_Agente = RequestBody['Nombre_Agente'],
            Email = RequestBody['Email'],
            Password = RequestBody['Password']
            )
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put (self, request, id):
        RequestBody = json.loads(request.body)
        Agentes = list(Agente.objects.filter(id=id).values())
        if len(Agentes) > 0:
            Agentes = Agente.objects.get(id=id)
            Agentes.Nombre_Agente = RequestBody['Nombre_Agente']
            Agentes.Email = RequestBody['Email']
            Agentes.Password = RequestBody['Password']
            Agentes.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Agente no encontrado"}
        return JsonResponse(datos)
    
    def delete (self, id):
        Agentes = list(Agente.objects.filter(id=id).values())
        if len(Agentes) > 0:
            Agente.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Agente no encontrado"}
        return JsonResponse(datos)
    