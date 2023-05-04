import OnlineGame
import OfflineGame

class GraphicalUI:
    def __init__(self, window):
        self.window = window
        self.new_game()

    def new_game(self):
        while True:
            try:
                self.window.game_type_popup()
                if self.window.game_type == "host":
                    OnlineGame.host_game(self.window.host_name, self.window.port_name, self)
                elif self.window.game_type == "connect":
                    OnlineGame.connect_to_game(self.window.host_name, self.window.port_name, self)
                elif self.window.game_type == "bot":
                    OfflineGame.play(self)
                break
            except Exception as error:
                self.handle_error(error)

    def start_game(self):
        self.window.clear()

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
        self.window.update()

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

        if self.window.after_game_popup():
            self.new_game()
        else:
            self.window.destroy()

    def handle_error(self, error):
        self.window.error_popup(error)

