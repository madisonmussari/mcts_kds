from players import HumanPlayer
from nim import str_to_action
from nim import Environment
from utils import play

if __name__ == "__main__":
    start_board = Environment([2, 3, 1], 0, 2)
    player1 = HumanPlayer(str_to_action)
    player2 = HumanPlayer(str_to_action)

    log = play(start_board, [player1, player2])
    print(log)