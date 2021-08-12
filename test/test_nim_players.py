from context import nim
from context import utils
from context import players


def test_perfect_player_vs_random_player():
    environment = nim.Environment([3, 4, 5], 0, 2)
    player_0 = nim.PerfectPlayer()
    player_1 = nim.RandomPlayer()

    log = utils.play(environment, [player_0, player_1])
    (last_environment, _, _) = log[-1]

    assert last_environment.is_terminal() == True
    assert last_environment.value(0) == 1
    assert last_environment.value(1) == -1


def test_random_player_vs_perfect_player():
    environment = nim.Environment([3, 4, 5], 0, 2)
    player_0 = nim.RandomPlayer()
    player_1 = nim.PerfectPlayer()

    log = utils.play(environment, [player_0, player_1])
    (last_environment, _, _) = log[-1]

    assert last_environment.is_terminal() == True
    assert last_environment.value(0) == -1
    assert last_environment.value(1) == 1

def test_perfect_player_vs_perfect_player():
    environment = nim.Environment([3, 4, 5], 0, 2)
    player_0 = nim.PerfectPlayer()
    player_1 = nim.PerfectPlayer()

    log = utils.play(environment, [player_0, player_1])
    (last_environment, _, _) = log[-1]

    assert last_environment.is_terminal() == True
    assert last_environment.value(0) == 1
    assert last_environment.value(1) == -1

def test_almost_perfect_player_vs_perfect_player_1():
    environment = nim.Environment([3, 4, 5], 0, 2)
    player_0 = nim.AlmostPerfectPlayer([])      # The player has no weaknesses
    player_1 = nim.PerfectPlayer()

    log = utils.play(environment, [player_0, player_1])
    (last_environment, _, _) = log[-1]

    assert last_environment.is_terminal() == True
    assert last_environment.value(0) == 1
    assert last_environment.value(1) == -1

def test_almost_perfect_player_vs_perfect_player_2():
    environment = nim.Environment([3, 4, 5], 0, 2)
    player_0 = nim.AlmostPerfectPlayer([[3, 4, 5]])      # The player has no weaknesses
    player_1 = nim.PerfectPlayer()

    log = utils.play(environment, [player_0, player_1])
    (last_environment, _, _) = log[-1]

    assert last_environment.is_terminal() == True
    assert last_environment.value(0) == -1
    assert last_environment.value(1) == 1


def test_perfect_player_vs_mcts_player():
    environment = nim.Environment([2, 3], 0, 2)
    player_0 = players.MctsPlayer()
    player_1 = nim.PerfectPlayer()

    for _ in range(10000):
        log = utils.play(environment, [player_0, player_1])
        (last_environment, _, _) = log[-1]
        game_value = [last_environment.value(k) for k in range(last_environment.num_agents())]
        player_0.cache[last_environment].backpropagation(game_value)

    player_0.exploration_param=0

    log = utils.play(environment, [player_0, player_1])
    (last_environment, _, _) = log[-1]

    assert last_environment.is_terminal() == True
    assert last_environment.value(0) == 1
    assert last_environment.value(1) == -1

def test_almost_perfect_player_vs_mcts_player():
    environment = nim.Environment([2, 3], 0, 2)
    player_0 = nim.AlmostPerfectPlayer([[2, 3]])
    player_1 = players.MctsPlayer()


    utils.play(environment, [player_1, player_0])
    for _ in range(1000):
        log = utils.play(environment, [player_0, player_1])
        (last_environment, _, _) = log[-1]
        game_value = [last_environment.value(k) for k in range(last_environment.num_agents())]
        player_1.cache[last_environment].backpropagation(game_value)
    
    player_1.exploration_param=0

    log = utils.play(environment, [player_0, player_1])
    (last_environment, _, _) = log[-1]

    assert last_environment.is_terminal() == True
    assert last_environment.value(0) == -1
    assert last_environment.value(1) == 1

def test_random_player_vs_mcts_player():
    environment = nim.Environment([2, 3], 0, 2)
    player_0 = players.MctsPlayer(exploration_param=0.5)
    player_1 = nim.RandomPlayer()
    player_2 = nim.PerfectPlayer()

    for _ in range(10000):
        log = utils.play(environment, [player_0, player_1])
        (last_environment, _, _) = log[-1]
        game_value = [last_environment.value(k) for k in range(last_environment.num_agents())]
        player_0.cache[last_environment].backpropagation(game_value)
    
    player_0.exploration_param=0
    
    for _ in range(10):
        log = utils.play(environment, [player_0, player_1])
        (last_environment, _, _) = log[-1]

        assert last_environment.is_terminal() == True
        assert last_environment.value(0) == 1
        assert last_environment.value(1) == -1

