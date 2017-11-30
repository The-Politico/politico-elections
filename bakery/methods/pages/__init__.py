from .state_executive_office import StateExecutiveOffice
from .special_election import SpecialElection


class EmptyHandler(object):
    """
    This class is necessary to bypass the inherited handle method exception
    from Django's BaseCommand.

    It *must* be the last inherited class.
    """
    def handle(self, *args, **kwargs):
        pass


class BakePagesMethods(
    StateExecutiveOffice,
    SpecialElection,
    EmptyHandler,
):
    pass
