import tkinter as tk
from abc import ABC, abstractmethod
import Utilities as util
import OnlineGame
import OfflineGame


class UI(ABC):
    """
    An abstract UI class.
    UIs provide the way for user to interact with the game.
    """

    @abstractmethod
    def new_game(self):
        """prepare for a new game. ask the user about the type of game (online, offline)."""

    @abstractmethod
    def start_game(self):
        """do the necessary procedures immediately after the start of the game."""

    @abstractmethod
    def make_guess(self):
        """
        request user to make their guess of the opponent's number

        Returns:
            str : the 4-digit number given by user
        """

    @abstractmethod
    def get_result(self, guess):
        """
        ask the user to answer opponent's query (say how many bulls & cows)

        Args:
            guess (str) : the opponent's guess

        Returns:
            tuple : the pair of two integers where the first is bulls and the second is cows
        """

    @abstractmethod
    def receive_result(self, result):
        """
        inform the user about the result of their query
       
        Args:
            result (tuple) : the result of the latest query. A pair of two integers where the first is bulls and the second is cows
       """

    @abstractmethod
    def wait(self):
        """wait for opponent to make their move"""

    @abstractmethod
    def end_game(self, i_won, opponent_won, moves):
        """
        end the game. inform user about the result.
        
        Args:
            i_won (bool) : did the user win?
            opponent_won (bool) : did the opponent win?
            moves (int) : the duration of the game in moves
        """

    @abstractmethod
    def handle_error(self, error):
        """
        handle any exceptions that occur

        Args:
            error : the error that occurred
        """


class BotUI(UI):
    """
    BotUI has the bot play and print the moves to console.
    Mostly for testing.

    Attributes:
        bot (Bot): the bot who is playing
    """

    def __init__(self, bot):
        self.bot = bot

    def new_game(self):
        print("Game started!")
        self.bot.start_game()

    def make_guess(self):
        while True:
            guess_str = self.bot.make_guess()
            print(f"Enter your guess (a {util.DIGIT_COUNT}-digit number): {guess_str}")
            if util.is_valid(guess_str):
                return guess_str

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


class ConsoleUI(UI):
    """
    Read and write in console.
    """

    def new_game(self):
        pass

    def start_game(self):
        print("Game started!")

    def make_guess(self):
        while True:
            guess_str = input(f"Enter your guess (a {util.DIGIT_COUNT}-digit number): ")
            if util.is_valid(guess_str):
                return guess_str

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


class GraphicalUI(UI):
    """
    User interacts with a graphical application.
    """

    def __init__(self, window):
        self.window = window
        self.new_game()

    def new_game(self):
        while True:
            try:
                self.window.game_type_popup()
                if self.window.game_type == "host":
                    OnlineGame.host_game(self.window.host_name, self.window.port_name, self)
                elif self.window.game_type == "connect":
                    OnlineGame.connect_to_game(self.window.host_name, self.window.port_name, self)
                elif self.window.game_type == "bot":
                    OfflineGame.play(self)
                break
            except tk.TclError:
                break
            except Exception as error:
                self.handle_error(error)

    def start_game(self):
        self.window.clear()

    def make_guess(self):
        self.window.set_message('Make your guess!')
        return self.window.opp_table.make_guess()

    def get_result(self, guess):
        self.window.set_message(f'Type how many bulls & cows in {guess}')
        return self.window.my_table.get_result(guess)

    def receive_result(self, result):
        self.window.opp_table.receive_result(result)

    def wait(self):
        self.window.set_message('Waiting for your opponent...')
        self.window.update()

    def end_game(self, i_won, opponent_won, moves):
        msg = f"Game over in {moves // 2} moves! "
        if i_won and not opponent_won:
            msg += "You won!"
        elif i_won and opponent_won:
            msg += "It's a draw"
        elif not i_won and opponent_won:
            msg += "Your opponent won :("
        elif not i_won and not opponent_won:
            msg += "It was abrupted"
            self.window.set_message(msg)

        if self.window.after_game_popup():
            self.new_game()
        else:
            self.window.destroy()

    def handle_error(self, error):
        self.window.error_popup(error)

