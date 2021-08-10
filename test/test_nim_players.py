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
    environment = nim.Environment([3, 4, 5], 0, 2)
    player_0 = players.MctsPlayer()
    player_1 = nim.PerfectPlayer()

    log = utils.play(environment, [player_0, player_1])
    (last_environment, _, _) = log[-1]

    assert last_environment.is_terminal() == True
    assert last_environment.value(0) == 1
    assert last_environment.value(1) == -1

def test_almost_perfect_player_vs_mcts_player():
    environment = nim.Environment([3, 4, 5], 0, 2)
    player_0 = nim.AlmostPerfectPlayer([3, 4, 5])
    player_1 = players.MctsPlayer()

    log = utils.play(environment, [player_0, player_1])
    (last_environment, _, _) = log[-1]

    assert last_environment.is_terminal() == True
    assert last_environment.value(0) == -1
    assert last_environment.value(1) == 1

def test_random_player_vs_mcts_player():
    environment = nim.Environment([2, 3, 4], 0, 2)
    player_0 = nim.RandomPlayer()
    player_1 = players.MctsPlayer()

    for _ in range(100):
        utils.play(environment, [player_1, player_1])
    
    for _ in range(5):
        log = utils.play(environment, [player_1, player_0])
        (last_environment, _, _) = log[-1]

        assert last_environment.is_terminal() == True
        assert last_environment.value(0) == 1
        assert last_environment.value(1) == -1

