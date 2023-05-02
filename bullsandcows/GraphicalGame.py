import OnlineGame
import OfflineGame
import Utilities as util
from MainWindow import MainWindow
from BullsAndCows import BullsAndCows
from ConsoleUI import ConsoleUI
from GraphicalUI import GraphicalUI
from Bot import Bot

if __name__ == "__main__":
    app = MainWindow()
    ui = GraphicalUI(app)
    if app.game_type == "host":
        OnlineGame.host_game(app.host_name, app.port_name, ui)
    elif app.game_type == "connect":
        OnlineGame.connect_to_game(app.host_name, app.port_name, ui)
    elif app.game_type == "bot":
        OfflineGame.play(ui)
    app.mainloop()
