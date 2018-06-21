from rest_framework import viewsets
from comentarios.models import Comentarios
from .serializers import ComentarioSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentarioSerializer