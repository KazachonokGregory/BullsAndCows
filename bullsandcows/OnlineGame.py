import socket
from Proxy import Proxy
from ConsoleUI import ConsoleUI
from BullsAndCows import BullsAndCows

def host_game(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    client, addr = server.accept()

    game = BullsAndCows(Proxy(client), ConsoleUI())

    game.host_game()
    game.start()

    server.close()

def connect_to_game(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    game = BullsAndCows(Proxy(client), ConsoleUI())

    game.connect_to_game()
    game.start()

