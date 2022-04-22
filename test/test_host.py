from unittest import TestCase

from src.contestant import Contestant
from src.host import Host
from test.test_common import doors_setup_winner_in_position


class TestHost(TestCase):

    def test_host_returns_door_0(self):

        doors_setup = doors_setup_winner_in_position(0)

        contestant = Contestant()
        contestant.first_choice = 1

        host = Host()

        door_by_host = host.door(contestant, doors_setup)
        self.assertEqual(2, door_by_host)

    def test_combinations(self):
        combinations = [
            {'contestant_choice': 0, 'winner_door': 1, 'host_door': 2},
            {'contestant_choice': 0, 'winner_door': 2, 'host_door': 1},

            {'contestant_choice': 1, 'winner_door': 0, 'host_door': 2},
            {'contestant_choice': 1, 'winner_door': 2, 'host_door': 0},

            {'contestant_choice': 2, 'winner_door': 0, 'host_door': 1},
            {'contestant_choice': 2, 'winner_door': 1, 'host_door': 0}
        ]

        for combination in combinations:

            winner_position = combination.get('winner_door')
            doors_setup = doors_setup_winner_in_position(winner_position)

            contestant = Contestant()
            contestant.first_choice = combination.get('contestant_choice')

            door_by_host = Host().door(contestant, doors_setup)
            self.assertEqual(combination.get('host_door'), door_by_host, f'Failed with: {combination}')
