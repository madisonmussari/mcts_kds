from mcts import tree_node
from nim import environment
from context import nim
from context import mcts


def make_expanded_node(heap=[3, 2, 4], current_player=0, num_players=2):
    environment = nim.Environment(heap, current_player, num_players)
    parent_node = tree_node.TreeNode(environment)

    parent_node.children = [
        tree_node.TreeNode(environment.what_if(action))
        for action in environment.valid_actions()
    ]

    return parent_node


# test the functions in the TreeNode class


def test_selection_1():
    parent_node = make_expanded_node()

    for count, child in enumerate(parent_node.children, 1):
        child.num_visits = 2 * count
        child.agent_to_value = [count, -count]
        parent_node.num_visits += 2 * count

    # Since all children have the same score, and exploreation parameter is different from zero,
    # we should explore the least visited child.
    expected_selection = {parent_node.children[0]}
    selected = set(parent_node.selection())
    assert expected_selection == selected


def test_selection_2():
    parent_node = make_expanded_node()

    for count, child in enumerate(parent_node.children, 1):
        child.num_visits = 2 * count
        child.agent_to_value = [-count, count]
        parent_node.num_visits += 2 * count

    # Since all children have the same score, and exploreation parameter is different from zero,
    # we should explore the least visited child.
    expected_selection = {parent_node.children[0]}
    selected = set(parent_node.selection())
    assert expected_selection == selected


def test_selection_3():
    parent_node = make_expanded_node()

    for count, child in enumerate(parent_node.children, 1):
        child.num_visits = 2 * count
        child.agent_to_value = [count, -count]
        parent_node.num_visits += 2 * count

    # Since all children have the same score, and exploreation parameter is zero,
    # All children are equally good.
    expected_selection = set(parent_node.children)
    selected = set(parent_node.selection(0))
    assert expected_selection == selected


def test_selection_4():
    parent_node = make_expanded_node()

    for count, child in enumerate(parent_node.children, 1):
        child.num_visits = count
        child.agent_to_value = [1, -1]
        parent_node.num_visits += count

    # With explorarion parameter equal to zero, we should select the best score (the first child)
    expected_selection = {parent_node.children[0]}
    selected = set(parent_node.selection(0))
    assert expected_selection == selected


def test_selection_5():
    parent_node = make_expanded_node(current_player=1)

    for count, child in enumerate(parent_node.children, 1):
        child.num_visits = count
        child.agent_to_value = [1, -1]
        parent_node.num_visits += count

    # With explorarion parameter equal to zero, we should select the best score (the last child)
    expected_selection = {parent_node.children[-1]}
    selected = set(parent_node.selection(0))
    assert expected_selection == selected


def test_expansion():
    # First example
    environment = nim.Environment([2, 3, 1], 0,
                                  2)  # should it instead be mcts.TreeNode?
    tree_node = mcts.TreeNode(environment)

    expected_children_before_expansion = {}
    real_children_before_expansion = set(tree_node.children)

    assert expected_children_before_expansion == real_children_before_expansion

    tree_node.expansion()
    expected_children_constructor = [([1, 3, 1], 1, 2), ([3, 1], 1, 2),
                                     ([2, 2, 1], 1, 2), ([2, 1, 1], 1, 2),
                                     ([2, 1], 1, 2), ([2, 3, 0], 1, 2)]
    expected_children_after_expansion = {
        mcts.TreeNode(nim.Environment(a[0], a[1], a[2]))
        for a in expected_children_constructor
    }
    assert set(tree_node.children) == expected_children_after_expansion

    # Second example
    environment = nim.Environment([2, 2, 2], 2, 3)
    tree_node = mcts.TreeNode(environment)

    expected_children_before_expansion = {}
    real_children_before_expansion = set(tree_node.children)

    assert expected_children_before_expansion == real_children_before_expansion

    tree_node.expansion()
    expected_children_constructor = {([1, 2, 2], 0, 3), ([2, 2], 0, 3),
                                     ([2, 1, 2], 0, 3), ([2, 2, 1], 0, 3)}
    expected_children_after_expansion = {
        mcts.TreeNode(nim.Environment(a[0], a[1], a[2]))
        for a in expected_children_constructor
    }
    assert set(tree_node.children) == expected_children_after_expansion


def test_backpropogation():
    node_0 = mcts.TreeNode([])
    node_1 = mcts.TreeNode([], parent=node_0)
    node_2 = mcts.TreeNode([], parent=node_1)
    node_3 = mcts.TreeNode([], parent=node_2)

    assert node_0.num_visits == 0
    assert node_1.num_visits == 0
    assert node_2.num_visits == 0
    assert node_3.num_visits == 0

    assert node_0.agent_to_value == []
    assert node_1.agent_to_value == []
    assert node_2.agent_to_value == []
    assert node_3.agent_to_value == []

    node_3.backpropagation([1, 0, -1])

    assert node_0.num_visits == 1
    assert node_1.num_visits == 1
    assert node_2.num_visits == 1
    assert node_3.num_visits == 1

    assert node_0.agent_to_value == [1, 0, -1]
    assert node_1.agent_to_value == [1, 0, -1]
    assert node_2.agent_to_value == [1, 0, -1]
    assert node_3.agent_to_value == [1, 0, -1]

    node_3.backpropagation([-1, 1, 1])

    assert node_0.num_visits == 2
    assert node_1.num_visits == 2
    assert node_2.num_visits == 2
    assert node_3.num_visits == 2

    assert node_0.agent_to_value == [0, 1, 0]
    assert node_1.agent_to_value == [0, 1, 0]
    assert node_2.agent_to_value == [0, 1, 0]
    assert node_3.agent_to_value == [0, 1, 0]

    node_3.backpropagation([-1, 1, 1])

    assert node_0.num_visits == 3
    assert node_1.num_visits == 3
    assert node_2.num_visits == 3
    assert node_3.num_visits == 3

    assert node_0.agent_to_value == [-1, 2, 1]
    assert node_1.agent_to_value == [-1, 2, 1]
    assert node_2.agent_to_value == [-1, 2, 1]
    assert node_3.agent_to_value == [-1, 2, 1]

    pass


def test_simulation():
    # An environment that always leads to a win
    heap = [1] * 5
    environment = nim.Environment(heap, 0, 2)
    tree_node = mcts.TreeNode(environment)

    expected_value = [1, -1]
    real_value = tree_node.simulation()
    assert expected_value == real_value

    # An environment that always leads to a loss
    heap = [1] * 6
    environment = nim.Environment(heap, 0, 2)
    tree_node = mcts.TreeNode(environment)

    expected_value = [-1, 1]
    real_value = tree_node.simulation()
    assert expected_value == real_value