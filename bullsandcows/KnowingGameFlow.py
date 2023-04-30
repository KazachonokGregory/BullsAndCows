import Utilities as util

# the player who knows the number is called the 'knowing' one

class KnowingGameFlow:
    def __init__(self):
        pass

    def set_number(self, number):
        self.number = number

    def receive_guess(self, number):
        return (util.get_bulls(number, self.number), util.get_cows(number, self.number))

