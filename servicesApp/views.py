from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Services
from .serializers import ServicesSerializer

# Create your views here.


class ServicesList(APIView):
    def get(self, request):
        services = Services.objects.all()
        data = ServicesSerializer(services, many=True).data
        return Response(data)


class ServicesDetail(APIView):
    def get(self, request, pk):
        service = Services.objects.get(pk=pk)
        data = ServicesSerializer(service).data
        return Response(data)
