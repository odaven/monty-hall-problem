from src.game_keep_strategy import game_keep_strategy
from src.results import Results


def play(iterations: int) -> dict:

    return {
        'results_keep_strategy': __run_games_keep_strategy(iterations),
        'results_change_strategy': __run_games_change_strategy(iterations)
    }


def __run_games_change_strategy(iterations) -> Results:
    results = Results()

    for _ in range(iterations):
        if game_keep_strategy():
            results.add_winner()
        else:
            results.add_loser()

    return results


def __run_games_keep_strategy(iterations) -> Results:
    results = Results()

    for _ in range(iterations):
        if game_keep_strategy():
            results.add_winner()
        else:
            results.add_loser()

    return results
