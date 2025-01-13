from rest_framework import serializers
from .models import Posts, Requests, StatusServices


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = '__all__'


class StatusServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusServices
        fields = '__all__'
