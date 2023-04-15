from .models import Agente, Asegurado, Cliente, Poliza, Estado_Poliza, Tipo_Poliza
from rest_framework import viewsets, permissions
from .serializers import AgenteSerializer, AseguradoSerializer, ClienteSerializer, PolizaSerializer, Estado_PolizaSerializer, Tipo_PolizaSerializer

class AgenteViewSet(viewsets.ModelViewSet):
    queryset = Agente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AgenteSerializer

class AseguradoViewSet(viewsets.ModelViewSet):
    queryset = Asegurado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AseguradoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer
    
class PolizaViewSet(viewsets.ModelViewSet):
    queryset = Poliza.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PolizaSerializer
    
class Estado_PolizaViewSet(viewsets.ModelViewSet):
    queryset = Estado_Poliza.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Estado_PolizaSerializer

class Tipo_PolizaViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Poliza.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Tipo_PolizaSerializer