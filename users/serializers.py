from rest_framework import serializers
from .models import Users, Ratings


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        # Campos visibles en la API
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'telephone', 'is_supplier', 'is_finder', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Crea un usuario con la contraseña encriptada"""
        user = Users.objects.create_user(**validated_data)
        return user


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'
