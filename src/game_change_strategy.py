from src.contestant import Contestant
from src.doors_setup import DoorsSetup
from src.host import Host


def game_change_strategy() -> bool:
    """
    Runs the change strategy

    1 - Contestant chooses a door
    2 - Host opens a non-winning door
    3 - Contestant opens the remaining door

    No need to now about the first choice here really
    """

    doors_setup = DoorsSetup()
    contestant = Contestant()

    host = Host()
    door_by_host = host.door(contestant, doors_setup)

    second_choice = contestant.second_choice(door_by_host)

    return doors_setup.doors[second_choice].winner
