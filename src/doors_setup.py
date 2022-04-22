import random

from src.door import Door


class DoorsSetup:

    def __init__(self):

        self.doors = [Door(), Door(), Door()]

        selected_as_a_winner = random.randint(0, 2)
        self.doors[selected_as_a_winner].winner = True
