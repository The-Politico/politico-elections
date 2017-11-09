from rest_framework import serializers

from election.models import Candidate, CandidateElection, Election, Party
from entity.models import Office, Person
from geography.models import Division
from vote.models import APElectionMeta
from vote.serializers import VotesSerializer


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
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        """Return object of images serialized by tag name."""
        return {str(i.tag): i.image.url for i in obj.images.all()}

    class Meta:
        model = Person
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'suffix',
            'images',
        )


class CandidateSerializer(FlattenMixin, serializers.ModelSerializer):
    party = serializers.SerializerMethodField()

    def get_party(self, obj):
        """Just party AP code."""
        return obj.party.ap_code

    class Meta:
        model = Candidate
        fields = (
            'party',
            'ap_candidate_id',
            'incumbent',
            'uid',
        )
        flatten = (
            ('person', PersonSerializer),
        )


class CandidateElectionSerializer(FlattenMixin, serializers.ModelSerializer):
    override_winner = serializers.SerializerMethodField()

    def get_override_winner(self, obj):
        vote = obj.votes.filter(division=obj.election.division).first()
        return vote.winning

    class Meta:
        model = CandidateElection
        fields = (
            'aggregable',
            'uncontested',
            'override_winner',
        )
        flatten = (
            ('candidate', CandidateSerializer),
        )


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = (
            'uid',
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
    candidates = serializers.SerializerMethodField()
    override_votes = serializers.SerializerMethodField()

    def get_override_votes(self, obj):
        if obj.meta.override_ap_votes:
            all_votes = None
            for ce in obj.candidate_elections.all():
                if all_votes:
                    all_votes = all_votes | ce.votes.all()
                else:
                    all_votes = ce.votes.all()
            return VotesSerializer(all_votes, many=True).data
        return False

    def get_candidates(self, obj):
        return CandidateElectionSerializer(
            obj.candidate_elections.all(),
            many=True
        ).data

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
            'uid',
            'date',
            'office',
            'primary_party',
            'division',
            'candidates',
            'override_votes',
        )
        flatten = (
            ('meta', APElectionMetaSerializer),
        )


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = (
            'uid',
            'slug',
            'label',
            'short_label',
            'ap_code',
        )
