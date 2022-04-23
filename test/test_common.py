from src.doors_setup import DoorsSetup


def doors_setup_winner_in_position(position: int) -> DoorsSetup:
    doors_setup = DoorsSetup()

    for door in doors_setup.doors:
        door.winner = False

    doors_setup.doors[position].winner = True

    return doors_setup
