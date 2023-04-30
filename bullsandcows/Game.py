import socket
import threading
import Utilities as util

class BullsAndCows:
 
    def __init__(self):
        self.my_guess = True
        self.i_won = False
        self.opponent_won = False
        self.game_over = False
        self.moves = 0

    def host_game(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)

        client, addr = server.accept()

        self.my_guess = True
        threading.Thread(target=self.handle_connection, args=(client,)).start()
        server.close()

    def connect_to_game(self, host, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        self.my_guess = False
        threading.Thread(target=self.handle_connection, args=(client,)).start()

    def handle_connection(self, client):
        print("Game has started!")
        while not self.game_over:
            if self.my_guess:
                self.my_guess = False
                self.moves += 1

                client.send(self.make_guess().encode('utf-8'))

                data = client.recv(1024)
                if not data:
                    break
                result = data.decode('utf-8')
                bulls, cows = map(int, result.split(','))
                print(f"There are {bulls} bulls and {cows} cows")

                if bulls == 4:
                    self.i_won = True
            else:
                self.my_guess = True
                self.moves += 1

                print("Waiting for opponent's guess...")
                data = client.recv(1024)
                if not data:
                    break
                guess = data.decode('utf-8')

                bulls, cows, result = self.give_result(guess)
                client.send(result.encode('utf-8'))

                if bulls == 4:
                    self.opponent_won = True
            
            if self.moves % 2 == 0 and self.i_won or self.opponent_won:
                break

        print(f"Game over in {self.moves // 2} moves!")
        if self.i_won and not self.opponent_won:
            print("You won!")
        elif self.i_won and self.opponent_won:
            print("It's a draw")
        elif not self.i_won and self.opponent_won:
            print("Your opponent won :(")
        elif not self.i_won and not self.opponent_won:
            print("It wasn't finished, unfortunately")

        client.close()

    """
    read player's guess and check it for validity
    """
    def make_guess(self):
        while True:
            try:
                guess_str = input("Enter your guess (a 4-digit number): ")
                guess = util.Number(int(guess_str))
                if not guess.is_valid():
                    raise ValueError
                return guess_str
            except ValueError:
                print("Invalid input")
                pass
    
    """
    read the result of the guess (how many bulls / cows have been guessed
    """
    def give_result(self, guess):
        while True:
            try:
                result = input(f"Your opponent says {guess}. How many bulls,cows ? ")
                bulls, cows = map(int, result.split(','))
                if bulls < 0 or cows < 0 or bulls + cows > 4:
                    raise ValueError
                return (bulls, cows, result)
            except ValueError:
                print("Invalid input")
                pass
