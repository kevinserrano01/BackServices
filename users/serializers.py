from rest_framework import serializers
from .models import Users, Ratings


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        # Campos visibles en la API
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'telephone', 'is_supplier', 'is_finder', 'image', 'created_at', 'updated_at','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Crea un usuario con la contraseña encriptada"""
        # Extraer la contraseña y la imagen antes de usar create_user
        password = validated_data.pop('password')
        image_profile = validated_data.pop('image', None)

        user = Users.objects.create_user(**validated_data)
        user.set_password(password)
        # Configurar la imagen de perfil, si está presente
        if image_profile:
            user.image = image_profile

        user.is_active = True
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.is_supplier = validated_data.get('is_supplier', instance.is_supplier)
        instance.is_finder = validated_data.get('is_finder', instance.is_finder)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

class RatingsSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True, required=True)   
    class Meta:
        model = Ratings
        fields = ['id', 'stars', 'comment','user_id']
        read_only_fields = ['user_id']
    def create(self, validated_data):
        rating = Ratings.objects.create(**validated_data)
        return rating
