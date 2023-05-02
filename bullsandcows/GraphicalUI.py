class GraphicalUI:
    def __init__(self, window):
        self.window = window

    def start_game(self):
        pass

    def make_guess(self):
        self.window.set_message('Make your guess!')
        return self.window.opp_table.make_guess()

    def get_result(self, guess):
        self.window.set_message(f'Type how many bulls & cows in {guess}')
        return self.window.my_table.get_result(guess)

    def receive_result(self, result):
        self.window.opp_table.receive_result(result)

    def wait(self):
        self.window.set_message('Waiting for your opponent...')

    def end_game(self, i_won, opponent_won, moves):
        msg = f"Game over in {moves // 2} moves! "
        if i_won and not opponent_won:
            msg += "You won!"
        elif i_won and opponent_won:
            msg += "It's a draw"
        elif not i_won and opponent_won:
            msg += "Your opponent won :("
        elif not i_won and not opponent_won:
            msg += "It was abrupted"
        self.window.set_message(msg)

