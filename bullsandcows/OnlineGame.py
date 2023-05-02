import socket
from Proxy import Proxy
from ConsoleUI import ConsoleUI
from GraphicalUI import GraphicalUI
from BullsAndCows import BullsAndCows

def host_game(host, port, ui):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    client, addr = server.accept()

    game = BullsAndCows(Proxy(client), ui)

    game.host_game()
    game.start()

    server.close()

def connect_to_game(host, port, ui):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    game = BullsAndCows(Proxy(client), ui)

    game.connect_to_game()
    game.start()

