from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from models import Agente
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import status


class AgenteView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        
        Agentes = list(Agente.objects.values())
        
        if (len(Agentes)>0):
            datos = {'message':"Usuario encontrado. ¡Login Exitoso!", 'Agentes': Agentes, 'status': status.HTTP_200_OK}
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

        datos = {'message': "Success", 'status': status.HTTP_201_CREATED}
        
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
            datos = {'message': "Sucess"}
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
    