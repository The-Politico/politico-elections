from django.contrib.contenttypes.models import ContentType

from theshow.models import PageContent


class SpecialElection(object):
    def bootstrap_special_election(self, election):
        division = election.division
        content_type = ContentType.objects.get_for_model(division)
        PageContent.objects.get_or_create(
            content_type=content_type,
            object_id=election.division.pk,
            election_day=election.election_day,
            special_election=True,
        )
