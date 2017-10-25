from rest_framework import viewsets

from .models import Election, Party
from .serializers import ElectionSerializer, PartySerializer


class ElectionViewSet(viewsets.ModelViewSet):
    serializer_class = ElectionSerializer
    queryset = Election.objects.all()


class PartyViewSet(viewsets.ModelViewSet):
    serializer_class = PartySerializer
    queryset = Party.objects.all()
