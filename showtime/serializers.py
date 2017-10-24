from rest_framework import serializers

from election.models import Party
from election.serializers import ElectionSerializer, PartySerializer
from entity.models import Body, Office
from geography.models import Division
from geography.serializers import DivisionSerializer


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
            'parties',
            'division',
            'elections',
        )


class BodySerializer(serializers.ModelSerializer):
    division = serializers.SerializerMethodField()
    parties = serializers.SerializerMethodField()
    # elections = serializers.SerializerMethodField()

    def get_division(self, obj):
        return DivisionSerializer(obj.jurisdiction.division).data

    def get_parties(self, obj):
        return PartySerializer(Party.objects.all(), many=True).data

    # def get_elections(self, obj):
    #     for office in obj.offices.all():
    #         for race in office.races.all():
    #             pass
    #     return ElectionSerializer(obj.offices.all(), many=True).data

    class Meta:
        model = Body
        fields = (
            'id',
            'parties',
            'division',
        )


class OfficeSerializer(serializers.ModelSerializer):
    division = serializers.SerializerMethodField()
    parties = serializers.SerializerMethodField()

    def get_division(self, obj):
        return DivisionSerializer(obj.division).data

    def get_parties(self, obj):
        return PartySerializer(Party.objects.all(), many=True).data

    class Meta:
        model = Office
        fields = (
            'id',
            'parties',
            'division',
        )
