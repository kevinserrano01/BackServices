from rest_framework import serializers
from .models import Posts, Requests, StatusServices
from users.serializers import UsersSerializer
from services.serializers import ServicesSerializer
from services.models import Services
from django.utils import timezone
from rest_framework.exceptions import ValidationError


class PostsSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)

    class Meta:
        model = Posts
        fields = '__all__'
        extra_kwargs = {
            # Hacer que el campo user sea de solo lectura
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        # Extraer el usuario autenticado del contexto
        user = self.context['request'].user
        if not user.is_supplier:
            raise serializers.ValidationError(
                "Only suppliers can create posts.")
        post = Posts.objects.create(user=user, **validated_data)
        return post


class RequestsSerializer(serializers.ModelSerializer):
    post = PostsSerializer(read_only=True)
    user = UsersSerializer(read_only=True)
    class Meta:
        model = Requests
        fields = '__all__'
        extra_kwargs = {'reason': {'required': False},
                        'user': {'read_only': True},
                        'post': {'read_only': True}}

    def create(self, validated_data):

        # Extraer los campos adicionales del contexto
        user = self.context['request'].user
        if not user.is_finder:
            raise serializers.ValidationError(
                "Only search engines can create requests.")

        post_id = self.context['request'].data.get('post_id')
        post = Posts.objects.get(id=post_id)
        if not post_id:
            raise serializers.ValidationError("post_id is required.")

        request = Requests.objects.create(post=post,user=user,
                                          **validated_data)  # Crear la solicitud
        return request

class StatusServicesSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)
    request = RequestsSerializer(read_only=True)
    class Meta:
        model = StatusServices
        fields = '__all__'

        extra_kwargs = {'user': {'required': False},
                        'request': {'read_only': True}, }
           
    def create(self, validated_data):
        user = self.context['request'].user
        request_id = self.context['request'].data.get('request')
        request = Requests.objects.get(id=request_id)
        status_services = StatusServices.objects.create(user=user, request=request, **validated_data)

        return status_services
    
    
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.dateupdated = timezone.now()
        instance.save()
        return instance
