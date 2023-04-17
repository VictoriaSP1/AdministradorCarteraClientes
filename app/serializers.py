from rest_framework import serializers
from .models import Agente, Asegurado, Cliente, Poliza, Estado_Poliza, Tipo_Poliza, Aseguradora

class AgenteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Agente
        fields = '__all__'
        
class AseguradoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Asegurado
        fields = '__all__'

class AseguradoraSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Aseguradora
        fields = '__all__'
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cliente
        fields = '__all__'
        
class PolizaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Poliza
        fields = '__all__'
        
class Estado_PolizaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Estado_Poliza
        fields = '__all__'

class Tipo_PolizaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Tipo_Poliza
        fields = '__all__'
        
    