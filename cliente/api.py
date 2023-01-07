from .models import Cliente, TipoCliente, Departamento, Municipio, Direccion
from rest_framework import viewsets, permissions
from .serializers import   ClienteSerializer, TipoClienteSerializer, DepartamentoSerializer, MunicipioSerializer, DireccionSerializer

class CLienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer
    
class TipoClienteViewSet(viewsets.ModelViewSet):
    queryset = TipoCliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class =TipoClienteSerializer
    
class DepartamentoViewSet(TipoClienteViewSet):
    queryset=Departamento.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class =DepartamentoSerializer
    
    
class MunicipioViewSet(viewsets.ModelViewSet):
    queryset=Municipio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class =MunicipioSerializer
    
class DireccionViewSet(viewsets.ModelViewSet):
    queryset=Direccion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class=DepartamentoSerializer
    
