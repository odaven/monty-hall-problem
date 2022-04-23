from unittest import TestCase
from unittest.mock import patch

from src.games.game_change_strategy import game_change_strategy
from test.test_common import doors_setup_winner_in_position


class TestGameChangeStrategy(TestCase):

    @patch('src.games.game_change_strategy.Host')
    @patch('src.games.game_change_strategy.Contestant')
    @patch('src.games.game_change_strategy.DoorsSetup')
    def test_game_change_selection_combinations(self, mocked_door_setup, mocked_contestant, mocked_host):
        combinations = [
            {'winner_door': 0, 'host_door': 1, 'second_choice': 0, 'result': True},
            {'winner_door': 0, 'host_door': 1, 'second_choice': 2, 'result': False},

            {'winner_door': 0, 'host_door': 2, 'second_choice': 0, 'result': True},
            {'winner_door': 0, 'host_door': 2, 'second_choice': 1, 'result': False},

            {'winner_door': 1, 'host_door': 0, 'second_choice': 1, 'result': True},
            {'winner_door': 1, 'host_door': 0, 'second_choice': 2, 'result': False},

            {'winner_door': 1, 'host_door': 2, 'second_choice': 0, 'result': False},
            {'winner_door': 1, 'host_door': 2, 'second_choice': 1, 'result': True},

            {'winner_door': 2, 'host_door': 0, 'second_choice': 1, 'result': False},
            {'winner_door': 2, 'host_door': 0, 'second_choice': 2, 'result': True},

            {'winner_door': 2, 'host_door': 1, 'second_choice': 0, 'result': False},
            {'winner_door': 2, 'host_door': 1, 'second_choice': 2, 'result': True}
        ]

        for combination in combinations:
            winner_position = combination.get('winner_door')
            mocked_door_setup.return_value = doors_setup_winner_in_position(winner_position)

            mocked_host.return_value.door.return_value = combination.get('host_door')

            mocked_contestant.return_value.second_choice.return_value = combination.get('second_choice')

            result = game_change_strategy()

            self.assertEqual(combination.get('result'), result, f'Failed with: {combination}')
