import Utilities as util

class ConsoleUI:
    def start_game(self):
        print("Game started!")

    """
    read player's guess and check it for validity
    """
    def make_guess(self):
        while True:
            guess_str = input(f"Enter your guess (a {util.DIGIT_COUNT}-digit number): ")
            if util.is_valid(guess_str):
                return guess_str

    """
    read the result of the guess (how many bulls / cows have been guessed
    """
    def get_result(self, guess):
        while True:
            try:
                result = input(f"Your opponent says {guess}. How many bulls,cows ? ")
                bulls, cows = map(int, result.split(','))
                if bulls < 0 or cows < 0 or bulls + cows > util.DIGIT_COUNT:
                    raise ValueError
                return result
            except ValueError:
                print("Invalid input")

    def receive_result(self, result):
        bulls, cows = map(int, result.split(','))
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
