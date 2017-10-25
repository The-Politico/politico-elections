from rest_framework import serializers
from rest_framework.reverse import reverse

from election.models import Election, ElectionDay, Party
from election.serializers import ElectionSerializer, PartySerializer
from entity.models import Body, Office
from geography.models import Division
from geography.serializers import DivisionSerializer


class ElectionDaySerializer(serializers.ModelSerializer):
    states = serializers.SerializerMethodField()
    bodies = serializers.SerializerMethodField()
    executive_offices = serializers.SerializerMethodField()

    def get_states(self, obj):
        return reverse(
            'state-election-list',
            request=self.context['request'],
            kwargs={'date': obj.date}
        )

    def get_bodies(self, obj):
        return reverse(
            'body-election-list',
            request=self.context['request'],
            kwargs={'date': obj.date}
        )

    def get_executive_offices(self, obj):
        return reverse(
            'office-election-list',
            request=self.context['request'],
            kwargs={'date': obj.date}
        )

    class Meta:
        model = ElectionDay
        fields = (
            'date',
            'cycle',
            'states',
            'bodies',
            'executive_offices',
        )


class StateListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse(
            'state-election-detail',
            request=self.context['request'],
            kwargs={
                'pk': obj.pk,
                'date': self.context['election_date']
            })

    class Meta:
        model = Division
        fields = (
            'url',
            'id',
            'name',
        )


class StateSerializer(serializers.ModelSerializer):
    division = serializers.SerializerMethodField()
    parties = serializers.SerializerMethodField()
    elections = serializers.SerializerMethodField()

    def get_division(self, obj):
        return DivisionSerializer(obj).data

    def get_parties(self, obj):
        return PartySerializer(Party.objects.all(), many=True).data

    def get_elections(self, obj):
        return ElectionSerializer(obj.elections.all(), many=True).data

    class Meta:
        model = Division
        fields = (
            'id',
            'elections',
            'parties',
            'division',
        )


class BodyListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse(
            'body-election-detail',
            request=self.context['request'],
            kwargs={
                'pk': obj.pk,
                'date': self.context['election_date']
            })

    class Meta:
        model = Division
        fields = (
            'url',
            'id',
            'name',
        )


class BodySerializer(serializers.ModelSerializer):
    division = serializers.SerializerMethodField()
    parties = serializers.SerializerMethodField()
    elections = serializers.SerializerMethodField()

    def get_division(self, obj):
        return DivisionSerializer(obj.jurisdiction.division).data

    def get_parties(self, obj):
        return PartySerializer(Party.objects.all(), many=True).data

    def get_elections(self, obj):
        election_day = ElectionDay.objects.get(
            date=self.context['election_date'])
        elections = Election.objects.filter(
            race__office__body=obj,
            election_day=election_day
        )
        return ElectionSerializer(elections, many=True).data

    class Meta:
        model = Body
        fields = (
            'id',
            'elections',
            'parties',
            'division',
        )


class OfficeListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse(
            'office-election-detail',
            request=self.context['request'],
            kwargs={
                'pk': obj.pk,
                'date': self.context['election_date']
            })

    class Meta:
        model = Division
        fields = (
            'url',
            'id',
            'name',
        )


class OfficeSerializer(serializers.ModelSerializer):
    division = serializers.SerializerMethodField()
    parties = serializers.SerializerMethodField()
    elections = serializers.SerializerMethodField()

    def get_division(self, obj):
        return DivisionSerializer(obj.division).data

    def get_parties(self, obj):
        return PartySerializer(Party.objects.all(), many=True).data

    def get_elections(self, obj):
        election_day = ElectionDay.objects.get(
            date=self.context['election_date'])
        elections = Election.objects.filter(
            race__office=obj,
            election_day=election_day
        )
        return ElectionSerializer(elections, many=True).data

    class Meta:
        model = Office
        fields = (
            'id',
            'elections',
            'parties',
            'division',
        )
