class Results:
    """ Storing results """

    def __init__(self):
        self.__winners = 0
        self.__losers = 0

    @property
    def winners(self) -> int:
        return self.__winners

    @property
    def losers(self) -> int:
        return self.__losers

    def add_winner(self) -> None:
        self.__winners += 1

    def add_loser(self) -> None:
        self.__losers += 1

    @property
    def winners_percentage(self) -> float:
        total = self.__winners + self.__losers
        return (self.__winners / total) * 100

    @property
    def losers_percentage(self) -> float:
        total = self.__winners + self.__losers
        return (self.__losers / total) * 100
