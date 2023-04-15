from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from models import Cliente
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
import json


class ClienteView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        Clientes = list(Cliente.objects.values())
        if (len(Clientes)>0):
            datos = {'message':"Success", 'Clientes': Clientes}
        else:
            datos = {'message': "Clientes no encontrados"}
        return JsonResponse(datos)
    
    def post(self, request):
        RequestBody = json.loads(request.body)
        Cliente.objects.create(
            Nombre_Cliente = RequestBody['Nombre_Cliente'],
            Email = RequestBody['Email'],
            Telefono = RequestBody['Telefono'],
            Id_Agente = RequestBody['Id_Agente']
            )
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put (self, request, id):
        RequestBody = json.loads(request.body)
        Clientes = list(Cliente.objects.filter(id=id).values())
        if len(Clientes) > 0:
            Clientes = Cliente.objects.get(id=id)
            Clientes.Nombre_Cliente = RequestBody['Nombre_Cliente']
            Clientes.Email = RequestBody['Email']
            Clientes.Telefono = RequestBody['Telefono']
            Clientes.Id_Agente = RequestBody['Id_Agente']
            Clientes.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Cliente no encontrado"}
        return JsonResponse(datos)
    
    def delete (self, id):
        Clientes = list(Cliente.objects.filter(id=id).values())
        if len(Clientes) > 0:
            Cliente.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Cliente no encontrado"}
        return JsonResponse(datos)
    