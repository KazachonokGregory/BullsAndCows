import Utilities as util
import random
import math

INF = 1e18

class InconsistentInputError(ValueError):
    pass

class Bot:
    def __init__(self):
        self.possible_numbers = None
        self.secret_number = None
        self.last_guess = None

    def start_game(self):
        self.possible_numbers = []
        for i in range(10 ** util.DIGIT_COUNT):
            if util.is_valid(str(i)):
                self.possible_numbers.append(str(i))
        random.shuffle(self.possible_numbers)
        self.secret_number = random.choice(self.possible_numbers)
        self.last_guess = None

    def make_guess(self):
        self.last_guess = self.possible_numbers[0]
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
        pass

class SmartBot(Bot):
    def make_guess(self):
        if self.last_guess is None:
            self.last_guess = self.possible_numbers[0]
            return self.last_guess

        max_entropy = -INF
        for guess in self.possible_numbers:
            distribution = {}
            for number in self.possible_numbers:
                result = util.get_result(number, guess)
                if (result not in distribution):
                    distribution.update({result:0})
                distribution[result] += 1

            entropy = 0
            for key, value in distribution.items():
                value /= len(self.possible_numbers)
                entropy -= value * math.log(value)

            if entropy > max_entropy:
                self.last_guess = guess
                max_entropy = entropy

        if len(self.possible_numbers) == 1:
            pass

        return self.last_guess

