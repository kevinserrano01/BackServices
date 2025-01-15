from rest_framework import serializers
from .models import Posts, Requests, StatusServices
from django.utils import timezone


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

    def create(self, validated_data):  # Extraer los campos adicionales del contexto
        # Extraer los campos adicionales del contexto
        user = validated_data.pop('user')
        # user = self.context['request'].user #esto es para extraer el usuario autenticado
        service = validated_data.pop('service')
        post = Posts.objects.create(
            user=user, service=service, **validated_data)  # Crear el post
        return post


class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ['message', 'status', 'reason', 'post_id', 'user_id']
        extra_kwargs = {'reason': {'required': False}}

    def create(self, validated_data):  # Extraer los campos adicionales del contexto
        # Extraer los campos adicionales del contexto
        user = self.context['request'].user
        if not user.is_finder:
            raise serializers.ValidationError(
                "Only search engines can create requests.")
        # Asegurar de que post_id esté en validated_data
        post_id = self.context['request'].data.get('post_id')
        if not post_id:
            raise serializers.ValidationError("post_id is required.")
        validated_data['post_id'] = post_id

        request = Requests.objects.create(
            **validated_data)  # Crear la solicitud
        return request

    def update(self, instance, validated_data):
        status = validated_data.get('status', instance.status)
        reason = validated_data.get('reason', instance.reason)
        if status == 'rejected' and not reason:
            raise serializers.ValidationError(
                "The reason is required when the status is 'rejected'.")
        instance.status = status
        instance.reason = reason
        instance.save()
        if status == 'accepted':
            StatusServices.objects.create(request=instance, status='accepted',
                                          comment='The search engine has accepted the request.', user=instance.user)
        return instance


class StatusServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusServices
        fields = '__all__'

    def create(self, validated_data):
        status_service = StatusServices.objects.create(**validated_data)
        return status_service

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.dateupdated = timezone.now()
        instance.save()
        return instance
