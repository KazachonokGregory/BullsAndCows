import OnlineGame
import OfflineGame
from ConsoleUI import ConsoleUI
import Utilities as util

if __name__ == "__main__":
    while True:
        game_type = input("Do you wish to host a game, connect to a game, or to play with a bot? Type 'host', 'connect', 'bot' accordingly\n")

        ui = ConsoleUI()
        if game_type == "bot":
            OfflineGame.play(ui)
        elif game_type == "host" or game_type == "connect":
            host, port = input("Type the host name and port separated by a space\n").split(" ")
            if game_type == "host":
                OnlineGame.host_game(host, int(port), ui)
            else:
                OnlineGame.connect_to_game(host, int(port), ui)
        else:
            print("Invalid input! Please choose a game type!")

