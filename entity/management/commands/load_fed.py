from django.core.management.base import BaseCommand

from entity.models import Body, Jurisdiction, Office
from geography.models import Division


class Command(BaseCommand):
    help = 'Loads basic structure of the federal governement. Must be run \
    *AFTER* load_geo.'

    def handle(self, *args, **options):
        USA = Division.objects.get(code='00')
        FED, created = Jurisdiction.objects.get_or_create(
            name="U.S. Federal Government",
            label="U.S. Federal Government",
            division=USA
        )
        Body.objects.get_or_create(
            name="U.S. Senate",
            label="U.S. Senate",
            jurisdiction=FED,
        )
        Body.objects.get_or_create(
            name="U.S. House of Representatives",
            label="U.S. House of Representatives",
            jurisdiction=FED,
        )
        Office.objects.get_or_create(
            name="President of the United States",
            label="President",
            jurisdiction=FED,
            division=USA,
        )
