from unittest import TestCase

from src.results import Results


class TestResults(TestCase):

    def test_results_count_winning(self):

        results = Results()

        self.assertEqual(0, results.winners)

        results.add_winner()

        self.assertEqual(1, results.winners)

    def test_results_count_losing(self):

        results = Results()

        self.assertEqual(0, results.losers)

        results.add_loser()

        self.assertEqual(1, results.losers)

    def test_winners_with_range(self):
        results = Results()

        for _ in range(1000):
            results.add_winner()

        self.assertEqual(1000, results.winners)

    def test_losers_with_range(self):
        results = Results()

        for _ in range(1000):
            results.add_loser()

        self.assertEqual(1000, results.losers)
