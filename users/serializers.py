from rest_framework import serializers
from .models import Users, Ratings


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        # Campos visibles en la API
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'telephone', 'is_supplier', 'is_finder', 'created_at', 'updated_at','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Crea un usuario con la contraseña encriptada"""
        password = validated_data.pop('password')
        user = Users.objects.create_user(**validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

class RatingsSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True, required=True)   
    class Meta:
        model = Ratings
        fields = ['id', 'stars', 'comment','user_id']
        read_only_fields = ['user_id']
    def create(self, validated_data):
        rating = Ratings.objects.create(**validated_data)
        return rating
