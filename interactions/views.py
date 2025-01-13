from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Posts, Requests, StatusServices
from .serializers import PostsSerializer, RequestsSerializer, StatusServicesSerializer

# Create your views here.


class PostsList(generics.ListCreateAPIView):
    """Vista para listar y crear posts"""
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar posts"""
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    lookup_field = 'id'  # Permite buscar por el campo 'id'


class RequestsList(generics.ListCreateAPIView):
    """Vista para listar y crear requests"""
    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer


class RequestsDetail(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar requests"""
    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer
    lookup_field = 'id'  # Permite buscar por el campo 'id'


class StatusServicesList(generics.ListCreateAPIView):
    """Vista para listar y crear status de servicios"""
    queryset = StatusServices.objects.all()
    serializer_class = StatusServicesSerializer


class StatusServicesDetail(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar status de servicios"""
    queryset = StatusServices.objects.all()
    serializer_class = StatusServicesSerializer
    lookup_field = 'id'  # Permite buscar por el campo 'id'
