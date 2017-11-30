from django.core.management.base import BaseCommand

from entity.models import Body, Jurisdiction, Office
from geography.models import Division


class Command(BaseCommand):
    help = 'Loads basic structure of the federal governement. Must be run \
    *AFTER* bootstrap_geography.'

    def handle(self, *args, **options):
        print('Loading the fed')
        USA = Division.objects.get(code='00')
        FED, created = Jurisdiction.objects.get_or_create(
            name="U.S. Federal Government",
            division=USA
        )
        Body.objects.get_or_create(
            slug="senate",
            name="U.S. Senate",
            jurisdiction=FED,
        )
        Body.objects.get_or_create(
            slug="house",
            name="U.S. House of Representatives",
            jurisdiction=FED,
        )
        Office.objects.get_or_create(
            slug="president",
            name="President of the United States",
            label="President",
            jurisdiction=FED,
            division=USA,
        )
        self.stdout.write(
            self.style.SUCCESS('Done.')
        )
