from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Users, Ratings
from .serializers import UsersSerializer, RatingsSerializer

# Create your views here.


class UsersList(generics.ListAPIView):
    """Vista para listar usuarios"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar usuarios"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'id'  # Permite buscar por el campo 'id'


class RatingsList(generics.ListCreateAPIView):
    """Vista para listar y crear ratings"""
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer


class RatingsDetail(generics.RetrieveUpdateDestroyAPIView):
    """Vista para ver, editar y eliminar ratings"""
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
    lookup_field = 'id'  # Permite buscar por el campo 'id'
