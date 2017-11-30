from decimal import Decimal
from subprocess import check_output

import requests
import simplejson as json
from django.core.management.base import BaseCommand

from core.aws import defaults, get_bucket
from geography.models import Division


class Command(BaseCommand):
    candidate_ids = {
        'Edward W. "Ed" Gillespie': '63881',
        'Ralph S. Northam': '63126',
        'Clifford D. Hyra': '65898'
    }
    parties = {
        'Democratic': 'Dem',
        'Republican': 'GOP',
        'Libertarian': 'Lib'
    }

    help = 'scrapes VA SOS'
    base_url = 'http://results.elections.virginia.gov/vaelections/'
    '2017%20November%20General/Json/'

    def handle(self, *args, **options):
        va = Division.objects.get(code='51')
        counties = va.children.all()
        data = []

        state_json = '{0}/Statewide.json'.format(self.base_url)
        r = requests.get(state_json)
        response = r.json()
        candidates = self.parse_data(response)
        for candidate in candidates:
            data.append(candidate)

        for county in counties:
            print(county.name, county.code)
            if county.code == '51097':
                url = '{0}/Locality/{1}/Index.json'.format(
                    self.base_url,
                    'KING%20&%20QUEEN%20COUNTY'
                )
            else:
                url = '{0}/Locality/{1}/Index.json'.format(
                    self.base_url,
                    county.name.upper().replace(' ', '%20')
                )
            r = requests.get(url)
            if r.status_code == 200:
                response = r.json()
                candidates = self.parse_data(response)
                for candidate in candidates:
                    data.append(candidate)

        with open('sos.json', 'w') as f:
            json.dump(data, f)

        bucket = get_bucket()
        bucket.put_object(
            Key='elections/2017/virginia/governor/results.json',
            ACL=defaults.ACL,
            Body=json.dumps(data),
            CacheControl=defaults.CACHE_HEADER,
            ContentType='application/json'
        )

        date = check_output('date')
        date_obj = {"date": date}
        bucket.put_object(
            Key='elections/2017/virginia/governor/last-updated.json',
            ACL=defaults.ACL,
            Body=json.dumps(date_obj),
            CacheControl=defaults.CACHE_HEADER,
            ContentType='application/json'
        )

    def parse_data(self, data):
        race_id = '47225'
        state_postal = 'VA'
        winner = False

        if not data.get('Locality'):
            fipscode = None
            level = 'state'
        else:
            if data['Locality']['LocalityCode'] == '515':
                fipscode = '51019'
            else:
                fipscode = '51{0}'.format(data['Locality']['LocalityCode'])
                level = 'county'

        for race in data['Races']:
            if race['RaceName'] == 'Governor':
                governor = race

        precincts_reporting = governor['PrecinctsReporting']
        precincts_total = governor['PrecinctsParticipating']
        precincts_reporting_pct = precincts_reporting / precincts_total

        candidates = []
        for candidate in governor['Candidates']:
            if candidate['BallotName'] == 'Write In':
                for written_c in candidates:
                    if written_c['polid'] == '65898':
                        written_c['votecount'] += candidate['Votes']
                        raw_writein_votepct = Decimal(
                            candidate['Percentage'].split('%')[0]
                        )
                        divided = raw_writein_votepct / 100
                        written_c['votepct'] += divided
                continue

            c_obj = {}
            c_obj['polid'] = self.candidate_ids[candidate['BallotName']]
            c_obj['party'] = self.parties[candidate['PoliticalParty']]
            c_obj['votecount'] = candidate['Votes']

            raw_votepct = Decimal(candidate['Percentage'].split('%')[0])
            c_obj['votepct'] = raw_votepct / 100

            c_obj['fipscode'] = fipscode
            c_obj['level'] = level
            c_obj['polnum'] = None
            c_obj['precinctsreporting'] = precincts_reporting
            c_obj['precinctsreportingpct'] = precincts_reporting_pct
            c_obj['precinctstotal'] = precincts_total
            c_obj['raceid'] = race_id
            c_obj['statepostal'] = state_postal
            c_obj['winner'] = winner

            candidates.append(c_obj)

        return candidates
