from unittest import TestCase
from unittest.mock import patch

from src.game_change_strategy import game_change_strategy
from test.test_common import doors_setup_winner_in_position


class TestGameChangeStrategy(TestCase):

    @patch('src.game_change_strategy.Contestant')
    @patch('src.game_change_strategy.DoorsSetup')
    def test_game_change_selection_win(self, mocked_door_setup, mocked_contestant):

        mocked_door_setup.return_value = doors_setup_winner_in_position(0)
        mocked_contestant.return_value.first_choice = 0

        result = game_change_strategy()

        self.assertTrue(result)
