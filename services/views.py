from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Services
from .serializers import ServicesSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class ServicesList(generics.ListCreateAPIView):
    """Vista para listar y crear servicios"""
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]  # Habilita el filtro
    # Campos por los que se puede filtrar
    filterset_fields = ['title', 'category']


class ServicesDetail(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar servicios"""
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    lookup_field = 'id'  # Permite buscar por el campo 'id'
    permission_classes = [IsAuthenticated]
