from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from entity.models import Body
from election.models import ElectionDay
from geography.models import Division


class PageContent(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=500)
    content_object = GenericForeignKey('content_type', 'object_id')
    election_day = models.ForeignKey(ElectionDay)
    division = models.ForeignKey(Division, null=True, blank=True)
    chatter = models.TextField()

    def get_body_content(self, body, election_day, division=None):
        body_type = ContentType.objects.get_for_model(body)

        kwargs = {
            'content_type__pk': body_type.pk,
            'object_id': body.pk,
            'election_day': election_day,
        }

        if division:
            kwargs['division'] = division

        return self.objects.filter(**kwargs)

    def get_office_content(self, office, election_day):
        office_type = ContentType.objects.get_for_model(office)

        return self.objects.filter(
            content_type__pk=office_type.pk,
            object_id=office.pk,
            election_day=election_day
        )

    def get_division_content(self, division, election_day):
        division_type = ContentType.objects.get_for_model(division)

        return self.objects.filter(
            content_type__pk=office_type.pk,
            object_id=division.pk,
            election_day=election_day
        )
