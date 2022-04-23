from src.participants.contestant import Contestant
from src.doors.doors_setup import DoorsSetup


def game_keep_strategy() -> bool:
    """
    Runs the keep strategy
    Door selected by the contestant is the one to be opened
    """

    doors_setup = DoorsSetup()
    contestant = Contestant()

    return doors_setup.doors[contestant.first_choice].winner
