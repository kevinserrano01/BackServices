from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import Posts, Requests, StatusServices, SavedPosts
from rest_framework.exceptions import PermissionDenied
from .serializers import PostsSerializer, RequestsSerializer, StatusServicesSerializer, SavedPostsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from users.models import Users


class PostsList(generics.ListCreateAPIView):
    """Vista para listar y crear posts"""
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Posts.objects.all()
        service_id = self.request.query_params.get('service', None)
        if service_id is not None:
            queryset = queryset.filter(service__id=service_id)
        return queryset

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
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_queryset(self):
        queryset = Requests.objects.all()
        user_id = self.request.query_params.get('user', None)
        print(user_id)
        if user_id is not None:
            profile = get_object_or_404(Users, id=user_id)
            print(profile)
            if profile.is_finder:
                queryset = queryset.filter(user=profile)
                print(queryset)
            if profile.is_supplier:
                queryset = queryset.filter(post__user_id=profile.id)
                print(queryset)
        return queryset

        

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

    def get_queryset(self):
        queryset = StatusServices.objects.all()
        request_id = self.request.query_params.get('request', None)
        if request_id is not None:
            queryset = queryset.filter(request__id=request_id)
        return queryset
    
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

class SavedPostsList(generics.ListCreateAPIView):
    """Vista para listar y crear posts guardados"""
    serializer_class = SavedPostsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtrar publicaciones guardas solo del usuario logueado
        user = self.request.user # Obtener al usuario logueado
        return SavedPosts.objects.filter(user=user) # Reemplaza 'user' con el campo adecuado en tu modelo

class SavedPostsDetail(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar posts guardados"""
    queryset = SavedPosts.objects.all()
    serializer_class = SavedPostsSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]