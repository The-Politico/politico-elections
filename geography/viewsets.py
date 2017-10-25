from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Division, DivisionLevel
from .serializers import DivisionSerializer

try:
    STATE_LEVEL = DivisionLevel.objects.get(name='state')
except:
    STATE_LEVEL = None


class ResultsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class DivisionViewSet(viewsets.ModelViewSet):
    serializer_class = DivisionSerializer
    queryset = Division.objects.all()
    pagination_class = ResultsPagination
