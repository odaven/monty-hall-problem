from src.contestant import Contestant
from src.doors_setup import DoorsSetup


def game_keep_strategy() -> bool:

    doors_setup = DoorsSetup()
    contestant = Contestant()

    return doors_setup.doors[contestant.first_choice].winner
