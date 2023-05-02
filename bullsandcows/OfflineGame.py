from BullsAndCows import BullsAndCows
from ConsoleUI import ConsoleUI
from GraphicalUI import GraphicalUI
from Bot import Bot
from MainWindow import MainWindow

def play(ui):
    bot = Bot()
    bot.start_game()
    game = BullsAndCows(bot, ui)

    game.host_game()
    game.start()
