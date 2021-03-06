import us
from rest_framework import serializers

from core.constants import DIVISION_LEVELS
from vote.models import Votes


class VotesSerializer(serializers.ModelSerializer):
    raceid = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()
    fipscode = serializers.SerializerMethodField()
    statepostal = serializers.SerializerMethodField()
    polid = serializers.SerializerMethodField()
    polnum = serializers.SerializerMethodField()
    winner = serializers.BooleanField(source='winning')
    precinctsreporting = serializers.SerializerMethodField()
    precinctsreportingpct = serializers.SerializerMethodField()
    precinctstotal = serializers.SerializerMethodField()
    votecount = serializers.IntegerField(source='count')
    votepct = serializers.FloatField(source='pct')

    def get_raceid(self, obj):
        """AP election ID."""
        return obj.candidate_election.election.meta.ap_election_id

    def get_level(self, obj):
        """DivisionLevel."""
        return obj.division.level.name

    def get_fipscode(self, obj):
        """County FIPS code"""
        if obj.division.level.name == DIVISION_LEVELS['county']:
            return obj.division.code
        return None

    def get_statepostal(self, obj):
        """State postal abbreviation if county or state else ``None``."""
        if obj.division.level.name == DIVISION_LEVELS['state']:
            return us.states.lookup(obj.division.code).abbr
        elif obj.division.level.name == DIVISION_LEVELS['county']:
            return us.states.lookup(obj.division.parent.code).abbr
        return None

    def get_polid(self, obj):
        """AP polid minus 'polid' prefix if polid else ``None``."""
        ap_id = obj.candidate_election.candidate.ap_candidate_id
        if 'polid-' in ap_id:
            return ap_id.replace('polid-', '')
        return None

    def get_polnum(self, obj):
        """AP polnum minus 'polnum' prefix if polnum else ``None``."""
        ap_id = obj.candidate_election.candidate.ap_candidate_id
        if 'polnum-' in ap_id:
            return ap_id.replace('polnum-', '')
        return None

    def get_precinctsreporting(self, obj):
        """Precincts reporting if vote is top level result else ``None``."""
        if obj.division.level == \
                obj.candidate_election.election.division.level:
            return obj.candidate_election.election.meta.precincts_reporting
        return None

    def get_precinctsreportingpct(self, obj):
        """
        Precincts reporting percent if vote is top level result else ``None``.
        """
        if obj.division.level == \
                obj.candidate_election.election.division.level:
            return obj.candidate_election.election.meta.precincts_reporting_pct
        return None

    def get_precinctstotal(self, obj):
        """Precincts total if vote is top level result else ``None``."""
        if obj.division.level == \
                obj.candidate_election.election.division.level:
            return obj.candidate_election.election.meta.precincts_total
        return None

    class Meta:
        model = Votes
        fields = (
            'raceid',
            'level',
            'fipscode',
            'statepostal',
            'polid',
            'polnum',
            'winner',
            'votecount',
            'votepct',
            'precinctsreporting',
            'precinctsreportingpct',
            'precinctstotal',
        )
