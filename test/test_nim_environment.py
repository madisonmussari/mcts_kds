from context import nim

def test_state():
    environment = nim.Environment([3, 2, 0], 1, 3)
    expected_environment = ((2, 3), 1, 3)
    assert environment.state() == expected_environment

    environment = nim.Environment([2, 3, 1], 1, 3)
    expected_environment = ((1, 2, 3), 1, 3)
    assert environment.state() == expected_environment

    environment = nim.Environment([2, 3, 1], 3, 3)  # NOTE: Maybe it is better to throw an error here
    expected_environment = ((1, 2, 3), 0, 3)
    assert environment.state() == expected_environment


def test_is_terminal():
    environment = nim.Environment([3], 1, 3)
    assert environment.is_terminal() == True

    environment = nim.Environment([2, 3, 1], 1, 3)
    assert environment.is_terminal() == False

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


def test_turn():
    environment = nim.Environment([2, 3, 1], 0, 3)
    assert environment.turn() == 0

    environment = nim.Environment([2, 3, 1], 1, 3)
    assert environment.turn() == 1

    environment = nim.Environment([2, 3, 1], 2, 3)
    assert environment.turn() == 2


def test_what_if():
    environment = nim.Environment([2, 3, 1], 0,
                                  3)  # current state ([1, 2, 3], 0, 3)
    environment = environment.what_if(
        (2, 1))  # Takes 1 stone of third heap (index 2)
    expected_state = ((1, 2, 2), 1, 3)
    assert expected_state == environment.state()

    environment = environment.what_if(
        (2, 1))  # Takes 1 stone of third heap (index 2)
    expected_state = ((1, 1, 2), 2, 3)
    assert expected_state == environment.state()

    environment = environment.what_if(
        (1, 1))  # Takes 1 stone of second heap (index 1)
    expected_state = ((1, 2), 0, 3)
    assert expected_state == environment.state()

    environment = environment.what_if((1, 3))  # Invalid move
    expected_state = ((1, 2), 0, 3)  # The environment does not change
    assert expected_state == environment.state()

    environment = environment.what_if(
        (1, 3))  # Takes 3 stone of second heap (index 1)
    expected_state = ((1, 2), 0, 3)  # Invalid move. Environment does not change.
    assert expected_state == environment.state()

    environment = environment.what_if(
        (0, 1))  # Takes 1 stone from first heap (index 0)
    expected_state = ((2,), 1, 3)
    assert expected_state == environment.state()

    environment = environment.what_if(
        (0, 1))  # The environment is final. Action not allowed
    expected_state = ((2,), 1, 3)  # State does not change
    assert expected_state == environment.state()

def test_valid_actions():
    environment = nim.Environment([2, 2, 3], 0, 3)
    expected_valid_actions = {(0, 1), (0, 2), (1, 1), (1, 2), (2, 1), (2, 2), (2, 3)}
    returned_valid_actions = {valid for valid in environment.valid_actions()}
    assert expected_valid_actions == returned_valid_actions


def test_num_agents():
    for num_players in range(1, 10):
        environment = nim.Environment([2, 2, 3], 0, num_players)
        assert environment.num_agents() == num_players


# Plays a full game of Nim
def test_simple_game():
    # Initial states
    environment = nim.Environment([2, 1, 3], 1, 3)

    assert environment.state() == ((1, 2, 3), 1, 3)
    assert environment.is_terminal() == False
    assert environment.turn() == 1

    valid_actions = {(0, 1), (1, 1), (1, 2), (2, 1), (2, 2), (2, 3)}
    environment_valid_actions = {x for x in environment.valid_actions()}
    print(environment.valid_actions())
    assert valid_actions == environment_valid_actions

    # First move, take 2 stones from heap 1 (second heap)
    environment = environment.what_if((1, 2))

    assert environment.state() == ((1, 3), 2, 3)
    assert environment.is_terminal() == False
    assert environment.turn() == 2

    valid_actions = {(0, 1), (1, 1), (1, 2), (1, 3)}
    environment_valid_actions = {x for x in environment.valid_actions()}
    assert valid_actions == environment_valid_actions

    # Checking that invalid moves don't change the environment
    environment = environment.what_if((0, 2))

    assert environment.state() == ((1, 3), 2, 3)
    assert environment.is_terminal() == False
    assert environment.turn() == 2

    valid_actions = {(0, 1), (1, 1), (1, 2), (1, 3)}
    environment_valid_actions = {x for x in environment.valid_actions()}
    assert valid_actions == environment_valid_actions

    # Second move, take 1 stone out of heap 0 (first heap)
    environment = environment.what_if((0, 1))
    assert environment.state() == ((3,), 0, 3) # FIXME this orginally was (3,1,[3])
    assert environment.is_terminal() == True
    assert environment.turn() == 0
    assert environment.value(0) == 1
    assert environment.value(1) == -1
    assert environment.value(2) == -1

    valid_actions = set()
    environment_valid_actions = {x for x in environment.valid_actions()}
    assert valid_actions == environment_valid_actions


def test_from_state():
    original_state = ((1, 2, 3), 1, 3)
    environment = nim.from_state(original_state)
    environment_state = environment.state()

    assert original_state == environment_state


def test_random_action():
    from math import sqrt
    from math import ceil

    environment = nim.Environment([3, 4, 5], 0, 2)

    actions_seen = dict()
    number_repetitions = 1000

    for _ in range(number_repetitions):
        current_action = environment.random_action()
        actions_seen[current_action] = actions_seen.get(current_action, 0) + 1
    
    total_number_of_actions = len([a for a in environment.valid_actions()])
    expected_number_of_actions = number_repetitions / total_number_of_actions
    prob = 1 / total_number_of_actions
    threshold = ceil(3 * sqrt(number_repetitions * prob * (1 - prob)))

    for repetions in actions_seen.values():
        assert abs(repetions - expected_number_of_actions) <= threshold

def test_eq():
    heap = [1,2,3]
    environment_1 = nim.Environment(heap,2,3)
    environment_2 = nim.Environment(heap,2,3)
    environment_3 = nim.Environment(heap,0,2)

    assert environment_1 == environment_2
    assert environment_1 != environment_3

def test_hash():
    heap = [1,2,3]
    environment_1 = nim.Environment(heap,2,3)
    environment_2 = nim.Environment(heap,2,3)
    environment_3 = nim.Environment(heap,0,2)

    assert hash(environment_1) == hash(environment_2)
    assert hash(environment_1) != hash(environment_3)