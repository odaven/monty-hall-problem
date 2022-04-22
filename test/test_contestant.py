from unittest import TestCase
from unittest.mock import patch

from src.contestant import Contestant


class TestContestant(TestCase):

    @patch('src.contestant.random.randint')
    def test_select_door_0(self, mocked_randint):
        mocked_randint.return_value = 0

        contestant = Contestant()

        self.assertEqual(0, contestant.first_choice)

    @patch('src.contestant.random.randint')
    def test_select_door_1(self, mocked_randint):
        mocked_randint.return_value = 1

        contestant = Contestant()

        self.assertEqual(1, contestant.first_choice)

    @patch('src.contestant.random.randint')
    def test_select_door_2(self, mocked_randint):
        mocked_randint.return_value = 2

        contestant = Contestant()

        self.assertEqual(2, contestant.first_choice)

    @patch('src.contestant.random.randint')
    def test_select_second_choice(self, mocked_randint):
        # By contestant
        mocked_randint.return_value = 0

        door_by_host = 1

        contestant = Contestant()
        second_choice = contestant.second_choice(door_by_host)

        self.assertEqual(2, second_choice)

    @patch('src.contestant.random.randint')
    def test_select_second_choice_combinations(self, mocked_randint):
        combinations = [
            {'first_choice': 0, 'door_by_host': 1, 'second_choice': 2},
            {'first_choice': 0, 'door_by_host': 2, 'second_choice': 1},

            {'first_choice': 1, 'door_by_host': 0, 'second_choice': 2},
            {'first_choice': 1, 'door_by_host': 2, 'second_choice': 0},

            {'first_choice': 2, 'door_by_host': 0, 'second_choice': 1},
            {'first_choice': 2, 'door_by_host': 1, 'second_choice': 0}
        ]

        for combination in combinations:

            # By contestant
            mocked_randint.return_value = combination.get('first_choice')

            door_by_host = combination.get('door_by_host')

            contestant = Contestant()
            second_choice = contestant.second_choice(door_by_host)

            self.assertEqual(combination.get('second_choice'), second_choice, f'Failed with: {combination}')
