import Utilities as util

class BotUI:
    def __init__(self, bot):
        self.moves = 0
        self.bot = bot

    def start_game(self):
        print("Game started!")
        self.bot.start_game()

    """
    read player's guess and check it for validity
    """
    def make_guess(self):
        self.moves += 1
        if self.moves > 10:
            raise ValueError()
        while True:
            guess_str = self.bot.make_guess()
            print(f"Enter your guess (a {util.DIGIT_COUNT}-digit number): {guess_str}")
            if util.is_valid(guess_str):
                return guess_str

    """
    read the result of the guess (how many bulls / cows have been guessed
    """
    def get_result(self, guess):
        while True:
            try:
                result = self.bot.get_result(guess)
                bulls, cows = map(int, result.split(','))
                print(f"Your opponent says {guess}. How many bulls,cows ? {result}")
                if bulls < 0 or cows < 0 or bulls + cows > util.DIGIT_COUNT:
                    raise ValueError
                return result
            except ValueError:
                print("Invalid input")

    def receive_result(self, result):
        bulls, cows = map(int, result.split(','))
        self.bot.receive_result(result)
        print(f"There are {bulls} bulls and {cows} cows")

    def wait(self):
        print("Waiting for your opponent...")

    def end_game(self, i_won, opponent_won, moves):
        print(f"Game over in {moves // 2} moves!")
        if i_won and not opponent_won:
            print("You won!")
        elif i_won and opponent_won:
            print("It's a draw")
        elif not i_won and opponent_won:
            print("Your opponent won :(")
        elif not i_won and not opponent_won:
            print("It wasn't finished, unfortunately")
