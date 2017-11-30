class SpecialElection(object):
    def fetch_special_elections(self):
        """
        Returns the unique divisions for all special elections on an
        election day.
        """
        return list(set([
            election.division for election in
            self.ELECTION_DAY.elections.filter(race__special=True)
        ]))
