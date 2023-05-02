import Utilities as util

class BullsAndCows:
 
    def __init__(self, client, ui):
        self.my_guess = True
        self.i_won = False
        self.opponent_won = False
        self.moves = 0
        self.client = client
        self.ui = ui

    def host_game(self):
        self.my_guess = True

    def connect_to_game(self):
        self.my_guess = False

    def start(self):
        self.ui.start_game()
        while not (self.moves % 2 == 0 and (self.i_won or self.opponent_won)):
            if self.my_guess:
                self.my_guess = False
                self.moves += 1

                guess = self.ui.make_guess()

                if not guess:
                    break

                result = self.client.get_result(guess)

                if not result:
                    break

                bulls, cows = map(int, result.split(','))
                self.ui.receive_result(result)

                if bulls == 4:
                    self.i_won = True
            else:
                self.my_guess = True
                self.moves += 1

                self.ui.wait()
                guess = self.client.make_guess()

                result = self.ui.get_result(guess)
                if not result:
                    break
                bulls, cows = map(int, result.split(','))
                self.client.receive_result(result)

                if bulls == 4:
                    self.opponent_won = True
            
        self.ui.end_game(self.i_won, self.opponent_won, self.moves)
        self.client.close()

    

