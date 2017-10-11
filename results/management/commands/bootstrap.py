import csv
import subprocess

from django.core.management.base import BaseCommand, CommandError
from results.models import (Geography, GeographyLevel, Election,
                        ElectionCycle, Office, Seat, Party,
                        ElectionType, Race, Person,
                        Candidate)

def _get_or_create_geography(row, level):
    return Geography.objects.get_or_create(
        code=row['fipscode'],
        state_fips=row['fipscode'][:1],
        geography_level=level
    )

def _get_or_create_geography_level(row):
    if row['level'] == 'national':
        code = 0
    elif row['level'] == 'state':
        code = 1
    elif row['level'] == 'district':
        code = 2
    elif row['level'] == 'county':
        code = 3
    else:
        code = 4


    return GeographyLevel.objects.get_or_create(
        label=row['level'],
        code=code
    )

def _get_or_create_election(row, election_cycle):
    return Election.objects.get_or_create(
        election_date=row['electiondate'],
        election_cycle=election_cycle
    )

def _get_or_create_election_cycle(year):
    return ElectionCycle.objects.get_or_create(
        label=year
    )

def _get_or_create_office(row):
    return Office.objects.get_or_create(
        label=row['officename'],
        office_level=0
    )

def _get_or_create_seat(row, office, geography):
    seat_label = row['seatname'] if row['seatname'] else row['officename']

    return Seat.objects.get_or_create(
        label=seat_label,
        seat_geography=geography,
        seat_office=office
    )

def _get_or_create_party(row):
    return Party.objects.get_or_create(
        ap_code=row['party']
    )

def _get_or_create_election_type(row):
    return ElectionType.objects.get_or_create(
        label=row['racetype']
    )


def _get_or_create_race(election, seat, party, election_type):
    return Race.objects.get_or_create(
        election=election,
        election_type=election_type,
        seat=seat,
        party=party
    )

def _get_or_create_person(row):
    return Person.objects.get_or_create(
        first_name=row['first'],
        last_name=row['last']
    )

def _get_or_create_candidate(row, person, party, race):
    return Candidate.objects.get_or_create(
        person=person,
        party=party,
        race=race,
        ap_candidate_id=row['candidateid']
    )


class Command(BaseCommand):
    help = 'populates models for a particular election date'

    def add_arguments(self, parser):
        parser.add_argument('election_date', type=str)

    def handle(self, *args, **options):
        with open('test.csv') as f:
            subprocess.run([
                'elex',
                'candidate_reporting_units',
                options['election_date']
            ], stdout=f)



            reader = csv.DictReader(f)

            for row in reader:
                level = _get_or_create_geography_level(row)[0]
                geography = _get_or_create_geography(row, level)[0]
                office = _get_or_create_office(row)[0]
                seat = _get_or_create_seat(row, office, geography)[0]
                election_cycle = _get_or_create_election_cycle('2018')[0]
                election = _get_or_create_election(row, election_cycle)[0]
                party = _get_or_create_party(row)[0]
                election_type = _get_or_create_election_type(row)[0]
                race = _get_or_create_race(election, seat, party, election_type)[0]
                person = _get_or_create_person(row)[0]
                candidate = _get_or_create_candidate(row, person, party, race)[0]
