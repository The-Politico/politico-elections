from rest_framework import serializers

from election.models import Candidate, Election, Party
from entity.models import Office, Person
from geography.models import Division
from vote.models import APElectionMeta


class FlattenMixin:
    """
    Flatens the specified related objects in this representation.

    Borrowing this clever method from:
    https://stackoverflow.com/a/41418576/1961614
    """
    def to_representation(self, obj):
        assert hasattr(self.Meta, 'flatten'), (
            'Class {serializer_class} missing "Meta.flatten" attribute'.format(
                serializer_class=self.__class__.__name__
            )
        )
        # Get the current object representation
        rep = super(FlattenMixin, self).to_representation(obj)
        # Iterate the specified related objects with their serializer
        for field, serializer_class in self.Meta.flatten:
            try:
                serializer = serializer_class(context=self.context)
                objrep = serializer.to_representation(getattr(obj, field))
                # Include their fields, prefixed, in the current representation
                for key in objrep:
                    rep[key] = objrep[key]
            except:
                continue
        return rep


class DivisionSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()

    def get_level(self, obj):
        return obj.level.slug

    class Meta:
        model = Division
        fields = (
            'code',
            'level'
        )


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'suffix',
        )


class CandidateSerializer(FlattenMixin, serializers.ModelSerializer):
    party = serializers.SerializerMethodField()

    def get_party(self, obj):
        return obj.party.ap_code

    class Meta:
        model = Candidate
        fields = (
            'party',
            'ap_candidate_id',
            'aggregable',
            'winner',
            'incumbent',
            'uncontested',
            'image',
        )
        flatten = (
            ('person', PersonSerializer),
        )


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = (
            'id',
            'slug',
            'name',
            'label',
            'short_label',
        )


class APElectionMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = APElectionMeta
        fields = (
            'ap_election_id',
            'called',
            'tabulated',
            'override_ap_call',
            'override_ap_votes',
        )


class ElectionSerializer(FlattenMixin, serializers.ModelSerializer):
    primary_party = serializers.SerializerMethodField()
    office = serializers.SerializerMethodField()
    candidates = CandidateSerializer(many=True, read_only=True)
    date = serializers.SerializerMethodField()
    division = DivisionSerializer()

    def get_primary_party(self, obj):
        if obj.party:
            return obj.party.ap_code
        return None

    def get_office(self, obj):
        return OfficeSerializer(obj.race.office).data

    def get_date(self, obj):
        return obj.election_day.date

    class Meta:
        model = Election
        fields = (
            'id',
            'date',
            'office',
            'primary_party',
            'division',
            'candidates',
        )
        flatten = (
            ('meta', APElectionMetaSerializer),
        )


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = (
            # 'id',
            'slug',
            'label',
            'short_label',
            'ap_code',
        )
