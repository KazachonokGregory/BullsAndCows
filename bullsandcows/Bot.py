import Utilities as util
import random

class InconsistentInputError(ValueError):
    pass

class Bot:
    def __init__(self):
        self.possible_numbers = None
        self.secret_number = None
        self.last_guess = None

    def start_game(self):
        self.possible_numbers = []
        for i in range(10000):
            if util.is_valid(str(i)):
                self.possible_numbers.append(str(i))
        self.secret_number = random.choice(self.possible_numbers)
        self.last_guess = None

    def make_guess(self):
        self.last_guess = random.choice(self.possible_numbers)
        return self.last_guess

    def get_result(self, guess):
        bulls = util.get_bulls(self.secret_number, guess)
        cows = util.get_cows(self.secret_number, guess)
        return str(bulls) + "," + str(cows)

    def receive_result(self, result):
        bulls, cows = map(int, result.split(','))
        self.possible_numbers = list(filter(lambda number: bulls == util.get_bulls(self.last_guess, number) and cows == util.get_cows(self.last_guess, number), self.possible_numbers))
        if len(self.possible_numbers) == 0:
            raise InconsistentInputError("The data given by player is inconsistent!")
        
    def wait(self):
        pass
    
    def end_game(self, i_won, opponent_won, moves):
        pass

    def close(self):
        print(f"Bot's secret number was {self.secret_number}")
