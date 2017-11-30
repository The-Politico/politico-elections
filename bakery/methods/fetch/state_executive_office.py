class StateExecutiveOffice(object):
    def fetch_state_executive_office_elections(self):
        return [
            election for election in
            self.ELECTION_DAY.elections.filter(race__special=False)
            if election.race.office.is_executive() and
            election.division.level == self.STATE_LEVEL
        ]
