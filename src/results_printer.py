from src.results import Results


def results_printer(results_dict: dict) -> None:

    __print('Keep strategy:', results_dict.get('results_keep_strategy'))
    __print('Change strategy:', results_dict.get('results_change_strategy'))


def __print(text: str, results: Results):

    # winners = results.winners
    winners_percentage = results.winners_percentage

    # losers = results.losers
    losers_percentage = results.losers_percentage

    print(f'{text} {winners_percentage}% winners - {losers_percentage}% losers')
