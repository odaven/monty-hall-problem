import random

from src.doors.door import Door


class DoorsSetup:
    """ A set of doors where one of them is randomly selected as the winner """

    def __init__(self):
        self.doors = [Door(), Door(), Door()]

        selected_as_a_winner = random.randint(0, 2)
        self.doors[selected_as_a_winner].winner = True
