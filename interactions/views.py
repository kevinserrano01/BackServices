from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import generics, serializers
from rest_framework import status
from .models import Posts, Requests, StatusServices
from services.models import Services
from rest_framework.exceptions import PermissionDenied
from .serializers import PostsSerializer, RequestsSerializer, StatusServicesSerializer
from services.serializers import ServicesSerializer

# Create your views here.


class PostsList(generics.ListCreateAPIView):
    """Vista para listar y crear posts"""
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar posts"""
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    lookup_field = 'id'  # Permite buscar por el campo 'id'
    permission_classes = [IsAuthenticated]


class RequestsList(generics.ListCreateAPIView):
    """Vista para listar y crear requests"""
    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer
    # Solo usuarios autenticados pueden crear requests
    # permission_classes = [IsAuthenticated]

    # Asociar la solicitud con el usuario autenticado al crearla
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status='pending',
                        post_id=self.request.data.get('post_id'))


class RequestsDetail(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar requests"""
    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer
    lookup_field = 'id'  # Permite buscar por el campo 'id'
    # Solo usuarios autenticados pueden visualizar, editar y eliminar requests
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        request = serializer.instance
        if self.request.user != request.post.user:
            raise PermissionDenied(
                "only the offeror can update the status of the request")
        serializer.save()


class StatusServicesList(generics.ListCreateAPIView):
    """Vista para listar y crear status de servicios"""
    queryset = StatusServices.objects.all()
    serializer_class = StatusServicesSerializer


class StatusServicesDetail(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar status de servicios"""
    queryset = StatusServices.objects.all()
    serializer_class = StatusServicesSerializer
    lookup_field = 'id'  # Permite buscar por el campo 'id'
    # Solo usuarios autenticados pueden visualizar, editar y eliminar status de servicios
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        status_service = serializer.instance
        if self.request.user != status_service.request.user and self.request.user != status_service.request.post.user:
            raise PermissionDenied(
                "only the offeror or the searcher can update the status of the application")
        serializer.save()
