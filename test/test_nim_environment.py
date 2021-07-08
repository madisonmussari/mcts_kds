import sys

sys.path.insert(0, '/Users/madison/mcts/nim')

from environment import Environment

# Write test functions for each of the methods of nim environment

def test_simple_game():
    # Initial states
    environment = Environment([2, 1, 3], 1, 3)

    assert environment.state() == (3, 1, [1, 2, 3])
    assert environment.is_terminal() == False
    assert environment.turn() == 1

    valid_actions = {(0,1), (1,1), (1,2) ,(2,1), (2,2), (2,3)}
    environment_valid_actions = {x for x in environment.valid_actions()}
    assert valid_actions == environment_valid_actions


    # First move, take 2 stones from heap 1 (second heap)
    environment = environment.what_if((1, 2))

    assert environment.state() == (3, 2, [1, 3])
    assert environment.is_terminal() == False
    assert environment.turn() == 2

    valid_actions = {(0,1), (1,1), (1,2) ,(1,3)}
    environment_valid_actions = {x for x in environment.valid_actions()}
    assert valid_actions == environment_valid_actions


    # Checking that invalid moves don't change the environment
    environment = environment.what_if((0, 2))

    assert environment.state() == (3, 2, [1, 3])
    assert environment.is_terminal() == False
    assert environment.turn() == 2

    valid_actions = {(0,1), (1,1), (1,2) ,(1,3)}
    environment_valid_actions = {x for x in environment.valid_actions()}
    assert valid_actions == environment_valid_actions

    # Second move, take 1 stone out of heap 0 (first heap)
    environment = environment.what_if((0, 1))
    assert environment.state() == (3, 1, [3])
    assert environment.is_terminal() == True
    assert environment.turn() == 0
    assert environment.value(0) == 1
    assert environment.value(1) == -1
    assert environment.value(2) == -1

    valid_actions = {}
    environment_valid_actions = {x for x in environment.valid_actions()}
    assert valid_actions == environment_valid_actions








