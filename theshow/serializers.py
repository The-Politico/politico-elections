from rest_framework import serializers
from rest_framework.reverse import reverse

from election.models import Election, ElectionDay, Party
from election.serializers import ElectionSerializer, PartySerializer
from entity.models import Body, Office
from geography.models import Division
from geography.serializers import DivisionSerializer

from .models import PageContent


class ElectionDaySerializer(serializers.ModelSerializer):
    states = serializers.SerializerMethodField()
    bodies = serializers.SerializerMethodField()
    executive_offices = serializers.SerializerMethodField()

    def get_states(self, obj):
        """States holding an election on election day."""
        return reverse(
            'state-election-list',
            request=self.context['request'],
            kwargs={'date': obj.date}
        )

    def get_bodies(self, obj):
        """Bodies with offices up for election on election day."""
        return reverse(
            'body-election-list',
            request=self.context['request'],
            kwargs={'date': obj.date}
        )

    def get_executive_offices(self, obj):
        """Executive offices up for election on election day."""
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
            'uid',
            'name',
        )


class StateSerializer(serializers.ModelSerializer):
    division = serializers.SerializerMethodField()
    parties = serializers.SerializerMethodField()
    elections = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    def get_division(self, obj):
        """Division."""
        return DivisionSerializer(obj).data

    def get_parties(self, obj):
        """All parties."""
        return PartySerializer(Party.objects.all(), many=True).data

    def get_elections(self, obj):
        """All elections in division."""
        return ElectionSerializer(obj.elections.all(), many=True).data

    def get_content(self, obj):
        """All content for a state's page on an election day."""
        election_day = ElectionDay.objects.get(
            date=self.context['election_date'])
        return PageContent.objects.division_content(election_day, obj)

    class Meta:
        model = Division
        fields = (
            'uid',
            'content',
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
            'uid',
            'name',
        )


class BodySerializer(serializers.ModelSerializer):
    division = serializers.SerializerMethodField()
    parties = serializers.SerializerMethodField()
    elections = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    def get_division(self, obj):
        """Division."""
        return DivisionSerializer(obj.jurisdiction.division).data

    def get_parties(self, obj):
        """All parties."""
        return PartySerializer(Party.objects.all(), many=True).data

    def get_elections(self, obj):
        """All elections held on an election day."""
        election_day = ElectionDay.objects.get(
            date=self.context['election_date'])
        elections = Election.objects.filter(
            race__office__body=obj,
            election_day=election_day
        )
        return ElectionSerializer(elections, many=True).data

    def get_content(self, obj):
        """All content for body's page on an election day."""
        election_day = ElectionDay.objects.get(
            date=self.context['election_date'])
        return PageContent.objects.body_content(election_day, obj)

    class Meta:
        model = Body
        fields = (
            'uid',
            'content',
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
            'uid',
            'name',
        )


class OfficeSerializer(serializers.ModelSerializer):
    division = serializers.SerializerMethodField()
    parties = serializers.SerializerMethodField()
    elections = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    def get_division(self, obj):
        """Division."""
        return DivisionSerializer(obj.division).data

    def get_parties(self, obj):
        """All parties."""
        return PartySerializer(Party.objects.all(), many=True).data

    def get_elections(self, obj):
        """All elections on an election day."""
        election_day = ElectionDay.objects.get(
            date=self.context['election_date'])
        elections = Election.objects.filter(
            race__office=obj,
            election_day=election_day
        )
        return ElectionSerializer(elections, many=True).data

    def get_content(self, obj):
        """All content for office's page on an election day."""
        election_day = ElectionDay.objects.get(
            date=self.context['election_date'])
        return PageContent.objects.office_content(election_day, obj)

    class Meta:
        model = Office
        fields = (
            'uid',
            'content',
            'elections',
            'parties',
            'division',
        )
