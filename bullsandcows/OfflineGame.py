from BullsAndCows import BullsAndCows
from ConsoleUI import ConsoleUI
from Bot import Bot

def play():
    bot = Bot()
    bot.start_game()
    game = BullsAndCows(bot, ConsoleUI())

    game.host_game()
    game.start()
