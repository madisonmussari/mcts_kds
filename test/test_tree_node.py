from context import nim
from context import mcts


def make_expanded_node(heap=[3, 2, 4], current_player=0, num_players=2):
    environment = nim.Environment(heap, current_player, num_players)
    parent_node = mcts.TreeNode(environment)

    for action in environment.valid_actions():
        child_environment = environment.what_if(action)
        child_node = mcts.TreeNode(child_environment, parent_node.cache)
        parent_node.children[action] = child_node
        parent_node.cache[child_environment] = child_node

    parent_node.is_expanded = True

    return parent_node


# test the functions in the TreeNode class
def test_selection_1():
    parent_node = make_expanded_node()

    actions = []
    for count, (action, child) in enumerate(parent_node.children.items(), 1):
        child.num_visits = 2 * count
        child.agent_to_value = [count, -count]
        parent_node.num_visits += 2 * count
        actions.append(action)

    # Since all children have the same score, and exploration parameter is different from zero, we should explore the least visited child.
    expected_selection = {actions[0]}
    selected = set(parent_node.selection())
    assert expected_selection == selected


def test_selection_2():
    parent_node = make_expanded_node()

    actions = []
    for count, (action, child) in enumerate(parent_node.children.items(), 1):
        child.num_visits = 2 * count
        child.agent_to_value = [-count, count]
        parent_node.num_visits += 2 * count
        actions.append(action)

    # Since all children have the same score, and exploreation parameter is different from zero, we should explore the least visited child.
    expected_selection = {actions[0]}
    selected = set(parent_node.selection())
    assert expected_selection == selected


def test_selection_3():
    parent_node = make_expanded_node()
    
    actions = []
    for count, (action, child) in enumerate(parent_node.children.items(), 1):
        child.num_visits = 2 * count
        child.agent_to_value = [count, -count]
        parent_node.num_visits += 2 * count
        actions.append(action)

    # Since all children have the same score, and exploration parameter is zero, all children are equally good.
    expected_selection = set(actions)
    selected = set(parent_node.selection(0))
    assert expected_selection == selected


def test_selection_4():
    parent_node = make_expanded_node()

    actions = []
    for count, (action, child) in enumerate(parent_node.children.items(), 1):
        child.num_visits = count
        child.agent_to_value = [1, -1]
        parent_node.num_visits += count
        actions.append(action)

    # With exploration parameter equal to zero, we should select the best score (the first child).
    expected_selection = {actions[0]}
    selected = set(parent_node.selection(0))
    assert expected_selection == selected


def test_selection_5():
    parent_node = make_expanded_node(current_player=1)
    
    actions = []
    for count, (action, child) in enumerate(parent_node.children.items(), 1):
        child.num_visits = count
        child.agent_to_value = [1, -1]
        parent_node.num_visits += count
        actions.append(action)

    # With exploration parameter equal to zero, we should select the best score (the last child).
    expected_selection = {actions[-1]}
    selected = set(parent_node.selection(0))
    assert expected_selection == selected


def test_expansion_1():
    environment = nim.Environment([2, 3, 1], 0, 2)
    root_node = mcts.TreeNode(environment)

    expected_children_before_expansion = set()
    real_children_before_expansion = set(root_node.children)

    assert expected_children_before_expansion == real_children_before_expansion
    assert root_node.is_expanded == False

    root_node.expansion()
    
    expected_expanded_node = make_expanded_node([2, 3, 1], 0, 2)

    for action, child_node in root_node.children.items():
        assert child_node.environment == expected_expanded_node.children[action].environment

    assert root_node.is_expanded == True

def test_expansion_2():
    environment = nim.Environment([2, 2, 2], 2, 3)
    root_node = mcts.TreeNode(environment)

    expected_children_before_expansion = set()
    real_children_before_expansion = set(root_node.children)

    assert expected_children_before_expansion == real_children_before_expansion
    assert root_node.is_expanded == False

    root_node.expansion()
    
    expected_expanded_node = make_expanded_node([2, 2, 2], 2, 3)

    for action, child_node in root_node.children.items():
        assert child_node.environment == expected_expanded_node.children[action].environment

    assert root_node.is_expanded == True


def test_backpropogation():
    environment = nim.Environment([2, 2, 2], 2, 3)
    node = mcts.TreeNode(environment)
    node.expansion()
    node.agent_to_value = [0, 0, 0]
    node.num_visits = 0
    
    num_visits = 0
    for _, child_node in node.children.items():
        child_node.backpropagation([1, 0, -1])
        num_visits += 1
    
    assert node.num_visits == num_visits
    assert node.agent_to_value == [num_visits, 0, - num_visits]


def test_simulation_1():
    # An environment that always leads to a win
    heap = [1] * 5
    environment = nim.Environment(heap, 0, 2)
    root_node = mcts.TreeNode(environment)

    expected_value = [1, -1]
    real_value = root_node.simulation()
    assert expected_value == real_value

def test_simulation_2():
    # An environment that always leads to a loss
    heap = [1] * 6
    environment = nim.Environment(heap, 0, 2)
    root_node = mcts.TreeNode(environment)

    expected_value = [-1, 1]
    real_value = root_node.simulation()
    assert expected_value == real_value
