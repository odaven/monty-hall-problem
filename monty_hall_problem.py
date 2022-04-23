from src.user_interface.input_request import input_request
from src.play import play
from src.user_interface.results_printer import results_printer


def main():
    tries = input_request()

    all_results = play(tries)

    results_printer(all_results)

if __name__ == "__main__":
    main()
