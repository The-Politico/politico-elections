from django.contrib.contenttypes.models import ContentType

from theshow.models import PageContent, PageType


def create_executive_office_page_content(self, election):
    """
    For executive offices, create page content for the office.

    For the president, create pages for each state result.
    """
    division = election.race.office.jurisdiction.division
    content_type = ContentType.objects.get_for_model(election.race.office)
    PageContent.objects.get_or_create(
        content_type=content_type,
        object_id=election.race.office.pk,
        election_day=election.election_day,
        division=division
    )
    if division.level == self.NATIONAL_LEVEL:
        self.create_federal_executive_state_pages_content(election)
    else:
        # Create state governor page type
        page_type, created = PageType.objects.get_or_create(
            model_type=ContentType.objects.get(
                app_label='entity',
                model='office'
            ),
            election_day=election.election_day,
            division_level=self.STATE_LEVEL,
        )
        PageContent.objects.get_or_create(
            content_type=ContentType.objects.get_for_model(page_type),
            object_id=page_type.pk,
            election_day=election.election_day,
        )
