from .models import Cliente
from rest_framework import viewsets, permissions
from .serializers import   ClienteSerializer

class CLienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer
    
