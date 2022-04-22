from unittest import TestCase

from src.strategy import Strategy


class TestStrategy(TestCase):

    def test_keep_selection(self):
        self.assertEqual('KEEP_SELECTION', Strategy.KEEP_SELECTION.name)
        self.assertEqual(0, Strategy.KEEP_SELECTION.value)

    def test_change_selection(self):
        self.assertEqual('CHANGE_SELECTION', Strategy.CHANGE_SELECTION.name)
        self.assertEqual(1, Strategy.CHANGE_SELECTION.value)
