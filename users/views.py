from urllib import request
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework import status
from .models import Users, Ratings
from .serializers import UsersSerializer, RatingsSerializer

# Create your views here.


class UserRegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """Método para crear un usuario con validacion"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Usuario creado exitosamente",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "message": "Error al crear el usuario",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class UsersList(generics.ListAPIView):
    """Vista para listar usuarios"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]


class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar usuarios"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'id'  # Permite buscar por el campo 'id'
    permission_classes = [IsAuthenticated]


class RatingsList(generics.ListCreateAPIView):
    """Vista para listar y crear ratings"""
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """Filtra ratings por usuario"""
        queryset = Ratings.objects.all()
        user_id = self.request.query_params.get('user', None)
        
        if user_id is not None:
            queryset = queryset.filter(user__id=user_id)
            
        return queryset


class RatingsDetail(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar ratings"""
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
    lookup_field = 'id'  # Permite buscar por el campo 'id'
    permission_classes = [IsAuthenticated]


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar el perfil de un usuario"""
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        # Validar si se envió la imagen en la solicitud
        image = request.FILES.get('image', None)
        if image:
            user.image = image
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Perfil actualizado exitosamente",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                "message": "Error al actualizar el perfil",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(
            {
                "message": "Perfil eliminado exitosamente"
            },
            status=status.HTTP_204_NO_CONTENT
        )
