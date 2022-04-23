from unittest import TestCase
from unittest.mock import patch

from src.doors.doors_setup import DoorsSetup


class TestDoorSetup(TestCase):

    def test_3_doors_initialised(self):
        door_setup = DoorsSetup()
        size = len(door_setup.doors)
        self.assertEqual(3, size)

    @patch('src.doors.doors_setup.random.randint')
    def test_1st_door_is_winner(self, randint_mocked):
        randint_mocked.return_value = 0

        door_setup = DoorsSetup()

        self.assertTrue(door_setup.doors[0].winner)
        self.assertFalse(door_setup.doors[1].winner)
        self.assertFalse(door_setup.doors[2].winner)

    @patch('src.doors.doors_setup.random.randint')
    def test_2nd_door_is_winner(self, randint_mocked):
        randint_mocked.return_value = 1

        door_setup = DoorsSetup()

        self.assertFalse(door_setup.doors[0].winner)
        self.assertTrue(door_setup.doors[1].winner)
        self.assertFalse(door_setup.doors[2].winner)

    @patch('src.doors.doors_setup.random.randint')
    def test_3rd_door_is_winner(self, randint_mocked):
        randint_mocked.return_value = 2

        door_setup = DoorsSetup()

        self.assertFalse(door_setup.doors[0].winner)
        self.assertFalse(door_setup.doors[1].winner)
        self.assertTrue(door_setup.doors[2].winner)
