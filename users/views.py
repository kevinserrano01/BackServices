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
    permission_classes = [IsAuthenticatedOrReadOnly]


class RatingsDetail(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar ratings"""
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
    lookup_field = 'id'  # Permite buscar por el campo 'id'
    permission_classes = [IsAuthenticated]
