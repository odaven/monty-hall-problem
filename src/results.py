class Results:
    def __init__(self):
        self.__winners = 0
        self.__losers = 0

    @property
    def winners(self):
        return self.__winners

    @property
    def losers(self):
        return self.__losers

    def add_winner(self):
        self.__winners += 1

    def add_loser(self):
        self.__losers += 1
