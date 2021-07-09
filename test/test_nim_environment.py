from context import nim

# Write test functions for each of the methods of nim environment


# Test state method
def test_state():
    environment = nim.Environment([2, 3, 1], 1, 3)
    expected_environment = (3, 1, [1, 2, 3])
    assert environment.state() == expected_environment

    environment = nim.Environment([2, 3, 1], 3, 3)
    expected_environment = (3, 0, [1, 2, 3])
    assert environment.state() == expected_environment


# Checks the is terminal method
def test_is_terminal():
    environment = nim.Environment([3], 1, 3)
    assert environment.is_terminal() == True

    environment = nim.Environment([2, 3, 1], 1, 3)
    assert environment.is_terminal() == False


# Checks value of terminal environments method
def test_value():
    environment = nim.Environment([2], 1, 3)
    assert environment.value(0) == -1
    assert environment.value(1) == 1
    assert environment.value(2) == -1
    assert environment.value(3) == None  # FIXME: Throw error

    environment = nim.Environment([2, 3, 1], 1, 3)
    assert environment.value(0) == None
    assert environment.value(1) == None
    assert environment.value(2) == None
    assert environment.value(3) == None  # FIXME: Throw error


# Tests turn method
def test_turn():
    environment = nim.Environment([2, 3, 1], 0, 3)
    assert environment.turn() == 0

    environment = nim.Environment([2, 3, 1], 1, 3)
    assert environment.turn() == 1

    environment = nim.Environment([2, 3, 1], 2, 3)
    assert environment.turn() == 2


# Test what_if method
def test_what_if():
    environment = nim.Environment([2, 3, 1], 0,
                                  3)  # current state (3, 0, [1, 2, 3])
    environment = environment.what_if(
        (2, 1))  # Takes 1 stone of third heap (index 2)
    expected_state = (3, 1, [1, 2, 2])
    assert expected_state == environment.state()

    environment = environment.what_if(
        (2, 1))  # Takes 1 stone of third heap (index 2)
    expected_state = (3, 2, [1, 1, 2])
    assert expected_state == environment.state()

    environment = environment.what_if(
        (1, 1))  # Takes 1 stone of second heap (index 1)
    expected_state = (3, 0, [1, 2])
    assert expected_state == environment.state()

    environment = environment.what_if((1, 3))  # Invalid move
    expected_state = (3, 0, [1, 2])  # The environment does not change
    assert expected_state == environment.state()

    environment = environment.what_if(
        (1, 3))  # Takes 3 stone of second heap (index 1)
    expected_state = (3, 0, [1,
                             2])  # Invalid move. Environment does not change.
    assert expected_state == environment.state()

    environment = environment.what_if(
        (0, 1))  # Takes 1 stone from first heap (index 0)
    expected_state = (3, 1, [2])
    assert expected_state == environment.state()

    environment = environment.what_if(
        (0, 1))  # The environment is final. Action not allowed
    expected_state = (3, 1, [2])  # State does not change
    assert expected_state == environment.state()


# Tests valid action  method
def test_valid_actions(self):
    environment = nim.Environment([1, 2, 3], 0, 3)
    expected_valid_actions = {(0, 1), (1, 1), (1, 2), (2, 1), (2, 2), (2, 3)}
    returned_valid_actions = {valid for valid in environment.valid_actions()}
    assert expected_valid_actions == returned_valid_actions


# Plays a full game of Nim
def test_simple_game():
    # Initial states
    environment = nim.Environment([2, 1, 3], 1, 3)

    assert environment.state() == (3, 1, [1, 2, 3])
    assert environment.is_terminal() == False
    assert environment.turn() == 1

    valid_actions = {(0, 1), (1, 1), (1, 2), (2, 1), (2, 2), (2, 3)}
    environment_valid_actions = {x for x in environment.valid_actions()}
    assert valid_actions == environment_valid_actions

    # First move, take 2 stones from heap 1 (second heap)
    environment = environment.what_if((1, 2))

    assert environment.state() == (3, 2, [1, 3])
    assert environment.is_terminal() == False
    assert environment.turn() == 2

    valid_actions = {(0, 1), (1, 1), (1, 2), (1, 3)}
    environment_valid_actions = {x for x in environment.valid_actions()}
    assert valid_actions == environment_valid_actions

    # Checking that invalid moves don't change the environment
    environment = environment.what_if((0, 2))

    assert environment.state() == (3, 2, [1, 3])
    assert environment.is_terminal() == False
    assert environment.turn() == 2

    valid_actions = {(0, 1), (1, 1), (1, 2), (1, 3)}
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
