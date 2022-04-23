from src.participants.contestant import Contestant
from src.doors.doors_setup import DoorsSetup


class Host:
    """
    The host will return the other not winning door
    """

    def door(self, contestant: Contestant, doors_setup: DoorsSetup) -> int:
        for index, door in enumerate(doors_setup.doors):
            if not door.winner and contestant.first_choice != index:
                return index
