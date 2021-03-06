from rest_framework import viewsets
from rest_framework.response import Response

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado = True)

    #def list(self, request, *args, **kwargs):
     #   return Response({'Lista':'xd'})