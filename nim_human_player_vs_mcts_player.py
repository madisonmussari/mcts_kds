from players import HumanPlayer
from players import MctsPlayer
from nim import str_to_action
from nim import Environment
import utils
from utils import play


if __name__ == "__main__":
    start_board = Environment([2, 3, 1], 0, 2)
    player1 = MctsPlayer(exploration_param=0.5)
    player2 = HumanPlayer(str_to_action)

    for _ in range(10000):
        log = utils.play(Environment, [player1, player1])
        (last_environment, _, _) = log[-1]
        game_value = [last_environment.value(k) for k in range(last_environment.num_agents())]
        player1.cache[last_environment].backpropagation(game_value)

    log = play(start_board, [player1, player2])
    print(log)