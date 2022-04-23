import random


class Contestant:
    """
    Contestant
    First choice is random
    Second choice is the free one considering the first choice and the selected by the host
    """

    def __init__(self):
        self.first_choice = random.randint(0, 2)

    def second_choice(self, door_by_host: int) -> int:
        for selection in [0, 1, 2]:
            if selection != self.first_choice and selection != door_by_host:
                return selection
