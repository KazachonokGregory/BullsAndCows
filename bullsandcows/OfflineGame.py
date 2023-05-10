from BullsAndCows import BullsAndCows
from Bot import Bot

def play(ui):
    bot = Bot()
    bot.start_game()
    game = BullsAndCows(bot, ui)

    game.host_game()
    game.start()
