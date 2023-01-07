from rest_framework import serializers
from .models import Cliente, TipoCliente, Departamento, Municipio, Direccion

class ClienteSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Cliente
        fields=('__all__')
        read_only_fields = ('create',)
        
class TipoClienteSerializer(serializers.ModelSerializer):
    class Meta: 
        model=TipoCliente
        fields=('__all__')
        read_only_fields = ('create',)

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Departamento
        fields=('__all__')
        read_only_fields = ('create',)
        
class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Municipio
        fields=('__all__')
        read_only_fields = ('create',)
        
class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Direccion
        fields=('__all__')
        read_only_fields = ('create',)
        

