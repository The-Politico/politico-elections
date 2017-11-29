from django.contrib.contenttypes.models import ContentType

from theshow.models import PageContent


def create_special_election_page_content(self, election):
    division = election.division
    content_type = ContentType.objects.get_for_model(division)
    PageContent.objects.get_or_create(
        content_type=content_type,
        object_id=election.division.pk,
        election_day=election.election_day,
        special_election=True,
    )
