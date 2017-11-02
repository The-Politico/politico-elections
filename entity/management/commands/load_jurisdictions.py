import us
from django.core.management.base import BaseCommand
from tqdm import tqdm

from entity.models import Jurisdiction
from geography.models import Division, DivisionLevel


class Command(BaseCommand):
    help = 'Loads federal and state jurisdictions. Must be run *AFTER* \
    load_geo.'

    def handle(self, *args, **options):
        print('Loading jurisdictions')
        USA = Division.objects.get(code='00')
        FED, created = Jurisdiction.objects.get_or_create(
            name="U.S. Federal Government",
            division=USA
        )
        state_level = DivisionLevel.objects.get(name='state')
        for state in tqdm(us.states.STATES):
            division = Division.objects.get(code=state.fips, level=state_level)
            name = '{} State Government'.format(state.name)
            if str(state.fips) == '11':
                name = 'Government of the District of Columbia'
            Jurisdiction.objects.get_or_create(
                name=name,
                division=division
            )
        self.stdout.write(
            self.style.SUCCESS('Done.')
        )
