from unittest import TestCase
from unittest.mock import patch

from src.game_keep_strategy import game_keep_strategy
from test.test_common import doors_setup_winner_in_position


class TestGameKeepStrategy(TestCase):

    @patch('src.game_keep_strategy.Contestant')
    @patch('src.game_keep_strategy.DoorsSetup')
    def test_game_keep_selection_win(self, mocked_door_setup, mocked_contestant):
        mocked_door_setup.return_value = doors_setup_winner_in_position(0)
        mocked_contestant.return_value.first_choice = 0

        result = game_keep_strategy()

        self.assertTrue(result)

    @patch('src.game_keep_strategy.Contestant')
    @patch('src.game_keep_strategy.DoorsSetup')
    def test_game_change_selection(self, mocked_door_setup, mocked_contestant):
        combinations = [
            {'winner_door': 0, 'first_choice': 0, 'winner': True},
            {'winner_door': 0, 'first_choice': 1, 'winner': False},
            {'winner_door': 0, 'first_choice': 2, 'winner': False},

            {'winner_door': 1, 'first_choice': 0, 'winner': False},
            {'winner_door': 1, 'first_choice': 1, 'winner': True},
            {'winner_door': 1, 'first_choice': 2, 'winner': False},

            {'winner_door': 2, 'first_choice': 0, 'winner': False},
            {'winner_door': 2, 'first_choice': 1, 'winner': False},
            {'winner_door': 2, 'first_choice': 2, 'winner': True},
        ]

        for combination in combinations:
            winner_position = combination.get('winner_door')
            doors_setup = doors_setup_winner_in_position(winner_position)
            mocked_door_setup.return_value.doors = doors_setup.doors

            mocked_contestant.return_value.first_choice = combination.get('first_choice')

            result = game_keep_strategy()

            self.assertEqual(combination.get('winner'), result, f'Failed with: {combination}')
