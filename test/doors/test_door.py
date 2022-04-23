from unittest import TestCase

from src.doors.door import Door


class TestDoor(TestCase):

    def test_by_default_is_winner_false(self):
        door = Door()
        self.assertFalse(door.winner)

    def test_winner_changes_value(self):
        door = Door()
        self.assertFalse(door.winner)

        door.winner = True
        self.assertTrue(door.winner)
