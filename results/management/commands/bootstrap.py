import csv
import results.models as models
import subprocess

from django.core.management.base import BaseCommand, CommandError
<<<<<<< Updated upstream
from results.models import (BallotAnswer, BallotMeasure, Candidate, Election,
                            ElectionCycle, Geography, GeoLevel, Office, Party,
                            Person, Race, RaceType, Seat)
=======
>>>>>>> Stashed changes


def _get_or_create_geography(row, level):
    if row['reportingunitname']:
        label = row['reportingunitname']
    else:
        label = row['statename']

    if level.code <= 1:
        return models.Geography.objects.get(
            label=label
        )
    else:
        return models.Geography.objects.get_or_create(
            code=row['fipscode'],
            state_fips=row['fipscode'][:2],
            geography_level=level,
            label=label
        )[0]


def _get_or_create_geography_level(row):
    if row['level'] == 'national':
        code = 0
    elif row['level'] == 'state':
        code = 1
    elif row['level'] == 'district':
        code = 2
    elif row['level'] == 'county' or row['level'] == 'township':
        code = 3
    else:
        code = 4


<<<<<<< Updated upstream
    return GeoLevel.objects.get_or_create(
=======
    return models.GeographyLevel.objects.get_or_create(
>>>>>>> Stashed changes
        label=row['level'],
        code=code
    )[0]


def _get_or_create_election_day(row, election_cycle):
    return models.Election_day.objects.get_or_create(
        date=row['electiondate'],
        cycle=election_cycle
    )[0]


def _get_or_create_election_cycle(year):
    return models.ElectionCycle.objects.get_or_create(
        label=year
    )[0]


def _get_or_create_body(row):
    return models.Body.objects.get_or_create(
        label=row['officename'],
        level=0
    )[0]

def _get_or_create_office(row, body, geography):
    office = '{0} {1}'.format(
        row['statename'],
        row['officename']
    )

    if row['seatname']:
        office_label = '{0}, {1}'.format(office, row['seatname'])
    else:
        office_label = office

    if row['level'] not in ['state', 'national']:
        return models.Office.objects.get(
            label=office_label,
            body__label=body.label,
            geography__state_fips=geography.state_fips
        )

    return models.Office.objects.get_or_create(
        label=office_label,
        geography=geography,
        office=office
    )[0]


def _get_or_create_party(row):
    return models.Party.objects.get_or_create(
        ap_code=row['party'],
        label=row['party']
    )[0]


def _get_or_create_election_type(row):
    return models.ElectionType.objects.get_or_create(
        label=row['racetype']
    )[0]


def _get_or_create_race(row, election, seat, race_type):
    if race_type.label not in ['General', 'Runoff']:
        if row['racetypeid'] in ['D', 'E']:
            party = models.Party.objects.get(ap_code='Dem')
        elif row['racetypeid'] in ['R', 'S']:
            party = models.Party.objects.get(ap_code='GOP')
        else:
            party = None
    else:
        party = None

    return models.Race.objects.get_or_create(
        election=election,
        race_type=race_type,
        seat=seat,
        party=party,
        ap_race_id=row['raceid']
    )[0]


def _get_or_create_person(row):
    return models.Person.objects.get_or_create(
        first_name=row['first'],
        last_name=row['last']
    )[0]


def _get_or_create_candidate(row, person, party, race):
    id_components = row['id'].split('-')
    candidate_id = '{0}-{1}'.format(
        id_components[1],
        id_components[2]
    )

    return models.Candidate.objects.get_or_create(
        person=person,
        party=party,
        race=race,
        ap_candidate_id=candidate_id
    )[0]


def _get_or_create_ballot_measure(row, geography, election):
    if row['level'] == 'state':
        state = geography
    else:
        state = models.Geography.objects.get(code=geography.state_fips)


    return models.BallotMeasure.objects.get_or_create(
        question=row['seatname'],
        label=row['seatname'],
        geography=state,
        election=election
    )[0]


def _get_or_create_ballot_answer(row, ballot_measure):
    return models.BallotAnswer.objects.get_or_create(
        answer=row['last'],
        label=row['last'],
        ballot_measure=ballot_measure
    )


def process_row(row):
    print('Processing {0} {1} {2} {3}'.format(
        row['statename'],
        row['level'],
        row['last'],
        row['officename']
    ))

    level = _get_or_create_geography_level(row)
    geography = _get_or_create_geography(row, level)
    election_cycle = _get_or_create_election_cycle('2018')
    election = _get_or_create_election(row, election_cycle)

    if row['is_ballot_measure'] == 'True':
        ballot_measure = _get_or_create_ballot_measure(row, geography, election)
        ballot_answer = _get_or_create_ballot_answer(row, ballot_measure)
    else:
        office = _get_or_create_office(row)
        seat = _get_or_create_seat(row, office, geography)
        party = _get_or_create_party(row)
        race_type = _get_or_create_race_type(row)
        race = _get_or_create_race(row, election, seat, race_type)
        person = _get_or_create_person(row)
        candidate = _get_or_create_candidate(row, person, party, race)



class Command(BaseCommand):
    help = 'populates models for a particular election date'

    def add_arguments(self, parser):
        parser.add_argument('election_date', type=str)

    def handle(self, *args, **options):
        writefile = open('test.csv', 'w')
        subprocess.run([
            'elex',
            'results',
            options['election_date'],
            '--national-only'
        ], stdout=writefile)

        with open('test.csv', 'r') as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                process_row(row)
