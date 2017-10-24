from rest_framework import serializers

from election.models import Party
from election.serializers import ElectionSerializer, PartySerializer

from .models import Division


class ChildDivisionSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()

    def get_level(self, obj):
        return obj.level.slug

    class Meta:
        model = Division
        fields = (
            'label',
            'short_label',
            'code',
            'code_components',
            'level',
        )


class DivisionSerializer(ChildDivisionSerializer):
    children = ChildDivisionSerializer(many=True, read_only=True)

    class Meta:
        model = Division
        fields = (
            'id',
            'label',
            'short_label',
            'code',
            'level',
            'code_components',
            'children',
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
            'parties',
            'division',
            'elections',
        )
