from .executive_office import ExecutiveOffice
from .legislative_office import LegislativeOffice
from .special_election import SpecialElection


class BootstrapContentMethods(
    ExecutiveOffice,
    LegislativeOffice,
    SpecialElection
):
    pass
