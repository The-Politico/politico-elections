from django.contrib.contenttypes.models import ContentType

from theshow.models import PageContent


class LegislativeOffice(object):
    def bootstrap_legislative_office(self, election):
        """
        For legislative offices, create page content for the legislative
        Body the Office belongs to AND the Division that corresponds to
        that Body's Jurisdiction.

        E.g., for a Texas state senate seat, create page content for:
            - Texas state senate page
            - Texas state page
        """
        body = election.race.office.body
        division = election.race.office.body.jurisdiction.division
        PageContent.objects.get_or_create(
            content_type=ContentType.objects.get_for_model(body),
            object_id=body.pk,
            election_day=election.election_day,
            division=division
        )
        PageContent.objects.get_or_create(
            content_type=ContentType.objects.get_for_model(division),
            object_id=division.pk,
            election_day=election.election_day,
        )
