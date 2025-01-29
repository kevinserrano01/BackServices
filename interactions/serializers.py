from rest_framework import serializers
from .models import Posts, Requests, StatusServices, SavedPosts
from users.serializers import UsersSerializer
from django.utils import timezone


class PostsSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)

    class Meta:
        """
        Representa un serializador de modelos Django para el modelo Posts.

        Esta clase define un serializador para el modelo Posts, especificando campos
        para incluir todos los atributos del modelo. Además, personaliza el manejo
        del campo 'user' haciéndolo de sólo lectura. Este serializador se puede utilizar
        para convertir instancias del modelo en formato JSON o para validar y guardar datos
        de entrada para el modelo.

        Attributes:
            Meta: Contiene opciones para el serializador, incluido el modelo
            a serializar, los campos a incluir, y cualquier argumento extra (p.e.,
            hacer que los campos sean de sólo lectura).
        """
        model = Posts
        fields = '__all__'
        extra_kwargs = {
            # Hacer que el campo user sea de solo lectura
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        """
        Crea una nueva entrada para un usuario proveedor basándose en los datos
        validados y el usuario autenticado del contexto de solicitud.

        Parameters:
            validated_data (dict): Los datos validados que contienen los campos
            necesarios para crear una nueva entrada.

        Raises:
            serializers.ValidationError: Si el usuario autenticado no es un proveedor.

        Returns:
            Posts: La instancia de publicación recién creada asociada al
            usuario proveedor autenticado.
        """
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

class SavedPostsSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)
    post = PostsSerializer(read_only=True)
    class Meta:
        model = SavedPosts
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True},
                        'post': {'read_only': True}}

    def create(self, validated_data):
        user = self.context['request'].user
        post_id = self.context['request'].data.get('post_id')
        post = Posts.objects.get(id=post_id)
        if not post_id:
            raise serializers.ValidationError("post_id is required.")
        saved_post = SavedPosts.objects.create(user=user, post=post, **validated_data)
        return saved_post