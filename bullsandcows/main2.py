from Game import BullsAndCows

if __name__ == "__main__":
    game = BullsAndCows()
    game.connect_to_game("localhost", 9997)
