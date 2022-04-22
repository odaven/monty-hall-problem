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
