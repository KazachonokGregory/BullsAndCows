from Number import Number, all_numbers

class GuesserGameState:
    def __init__():
        moves = []
        possible_numbers = all_numbers

    def make_move(said_number, cows, bulls):
        moves.append(said_number)
        possible_numbers = filter(lambda number: \
                get_cows(number, said_number) == cows and \
                get_bulls(number, said_number) == bulls, \
                possible_numbers)

