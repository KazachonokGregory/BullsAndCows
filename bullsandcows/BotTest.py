import Bot
from BullsAndCows import BullsAndCows
import Utilities as util
from BotUI import BotUI
import time

"""
The most intelligent game ever played
"""
if __name__ == "__main__":
    while (True):
        good_boy = Bot.SmartBot()
        bad_boy = Bot.Bot()

        ui = BotUI(good_boy)
        game = BullsAndCows(bad_boy, ui)
        game.host_game()
        bad_boy.start_game()
        game.start()
        print()
        time.sleep(1)
