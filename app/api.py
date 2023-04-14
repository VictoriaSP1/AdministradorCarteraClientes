from .models import Agente
from rest_framework import viewsets, permissions
from .serializers import AgenteSerializer

class AgenteViewSet(viewsets.ModelViewSet):
    queryset = Agente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AgenteSerializer

