from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Services
from .serializers import ServicesSerializer

# Create your views here.


class ServicesList(generics.ListCreateAPIView):
    """Vista para listar y crear servicios"""
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesDetail(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar servicios"""
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    lookup_field = 'id'  # Permite buscar por el campo 'id'
