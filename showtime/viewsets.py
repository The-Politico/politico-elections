from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from entity.models import Body, Office
from geography.models import Division, DivisionLevel

from .serializers import BodySerializer, OfficeSerializer, StateSerializer

STATE_LEVEL = DivisionLevel.objects.get(name='state')


class ResultsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = Division.objects.filter(level=STATE_LEVEL)
    pagination_class = ResultsPagination


class BodyViewSet(viewsets.ModelViewSet):
    serializer_class = BodySerializer
    queryset = Body.objects.all()
    pagination_class = ResultsPagination


class OfficeSerializer(viewsets.ModelViewSet):
    serializer_class = OfficeSerializer
    queryset = Office.objects.all()
