from rest_framework import generics
from rest_framework.exceptions import APIException
from rest_framework.pagination import PageNumberPagination

from election.models import ElectionDay
from entity.models import Body, Office
from geography.models import Division, DivisionLevel

from .serializers import (BodyListSerializer, BodySerializer,
                          ElectionDaySerializer, OfficeListSerializer,
                          OfficeSerializer, SpecialElectionListSerializer,
                          SpecialElectionSerializer, StateListSerializer,
                          StateSerializer)

try:
    STATE_LEVEL = DivisionLevel.objects.get(name='state')
except:
    STATE_LEVEL = None


class ResultsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ElectionDayList(generics.ListAPIView):
    serializer_class = ElectionDaySerializer
    queryset = ElectionDay.objects.all()


class ElectionDayDetail(generics.RetrieveAPIView):
    serializer_class = ElectionDaySerializer
    queryset = ElectionDay.objects.all()


class StateMixin(object):
    def get_queryset(self):
        """
        Returns a queryset of all states holding a non-special election on
        a date.
        """
        try:
            date = ElectionDay.objects.get(date=self.kwargs['date'])
        except:
            raise APIException(
                'No elections on {}.'.format(self.kwargs['date'])
            )
        division_ids = []
        for election in date.elections.all():
            if election.division.level == STATE_LEVEL and \
                    not election.race.special:
                division_ids.append(election.division.uid)
        return Division.objects.filter(uid__in=division_ids)

    def get_serializer_context(self):
        """Adds ``election_day`` to serializer context."""
        context = super(StateMixin, self).get_serializer_context()
        context['election_date'] = self.kwargs['date']
        return context


class StateList(StateMixin, generics.ListAPIView):
    serializer_class = StateListSerializer


class StateDetail(StateMixin, generics.RetrieveAPIView):
    serializer_class = StateSerializer


class SpecialMixin(object):
    def get_queryset(self):
        """
        Returns a queryset of all states holding a special election on a date.
        """
        try:
            date = ElectionDay.objects.get(date=self.kwargs['date'])
        except:
            raise APIException(
                'No elections on {}.'.format(self.kwargs['date'])
            )
        division_ids = []
        for election in date.elections.all():
            if election.division.level == STATE_LEVEL and \
                    election.race.special:
                division_ids.append(election.division.uid)
        return Division.objects.filter(uid__in=division_ids)

    def get_serializer_context(self):
        """Adds ``election_day`` to serializer context."""
        context = super(SpecialMixin, self).get_serializer_context()
        context['election_date'] = self.kwargs['date']
        return context


class SpecialList(SpecialMixin, generics.ListAPIView):
    serializer_class = SpecialElectionListSerializer


class SpecialDetail(SpecialMixin, generics.RetrieveAPIView):
    serializer_class = SpecialElectionSerializer


class BodyMixin(object):
    def get_queryset(self):
        """
        Returns a queryset of all bodies holding an election on a date.
        """
        try:
            date = ElectionDay.objects.get(date=self.kwargs['date'])
        except:
            raise APIException(
                'No elections on {}.'.format(self.kwargs['date'])
            )
        body_ids = []
        for election in date.elections.all():
            body = election.race.office.body
            if body:
                body_ids.append(body.uid)
        return Body.objects.filter(uid__in=body_ids)

    def get_serializer_context(self):
        """Adds ``election_day`` to serializer context."""
        context = super(BodyMixin, self).get_serializer_context()
        context['election_date'] = self.kwargs['date']
        return context


class BodyList(BodyMixin, generics.ListAPIView):
    serializer_class = BodyListSerializer


class BodyDetail(BodyMixin, generics.RetrieveAPIView):
    serializer_class = BodySerializer


class OfficeMixin(object):
    def get_queryset(self):
        """
        Returns a queryset of all executive offices holding an election on
        a date.
        """
        try:
            date = ElectionDay.objects.get(date=self.kwargs['date'])
        except:
            raise APIException(
                'No elections on {}.'.format(self.kwargs['date'])
            )
        office_ids = []
        for election in date.elections.all():
            office = election.race.office
            if not office.body:
                office_ids.append(office.uid)
        return Office.objects.filter(uid__in=office_ids)

    def get_serializer_context(self):
        """Adds ``election_day`` to serializer context."""
        context = super(OfficeMixin, self).get_serializer_context()
        context['election_date'] = self.kwargs['date']
        return context


class OfficeList(OfficeMixin, generics.ListAPIView):
    serializer_class = OfficeListSerializer


class OfficeDetail(OfficeMixin, generics.RetrieveAPIView):
    serializer_class = OfficeSerializer
